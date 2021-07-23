import pandas as pd
import os
from tqdm.auto import tqdm

import spacy
from spacy.pipeline import EntityRuler
import stanza

# from datetime_extractor import DateTimeExtractor
# from date_extractor import extract_dates
# from date_extractor import extract_date
# import datefinder
# from dateparser.search import search_dates

import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def main():
    file_path = os.path.join('160_links_cleaned.csv')
    df = pd.read_csv(file_path, sep=',', engine='python')

    nlp_spacy = spacy.load('en_core_web_lg')
    nlp_stanza = stanza.Pipeline('en')

    # add custom entity to spacy
    ruler = EntityRuler(nlp_spacy, overwrite_ents=True)

    # load companies list
    print('loading company names')
    file_path = os.path.join('company_names_nasdaq.csv')
    df = pd.read_csv(file_path, sep=',', engine='python')
    companies = list(df['name'])

    # tag companies
    for item in companies:
        ruler.add_patterns([{"label": "ORG", "pattern": item}])

    # tag periods
    periods = ["q1", "q2", "q3", "q4",
               "1q", "2q", "3q", "4q",
               "quarter 1", "quarter 2", "quarter 3", "quarter 4",
               "first quarter", "second quarter", "third quarter", "fourth quarter",
               "full year", "annual", "1s", "2s",
               "s1", "s2", "first half", "second half", ]
    for item in periods:
        ruler.add_patterns([{"label": "FISCAL_PERIOD", "pattern": item}])

    # add custom rules to the pipe
    nlp_spacy.add_pipe(ruler)
    all_names = []
    all_dates = []
    all_times = []
    all_fp = []

    for url in urls:
        company_name = extract_company(url, nlp_spacy, nlp_stanza)
        company_name_2 = get_company(raw_event_text, nlp_spacy, nlp_stanza)
        text_date, text_time = get_date_time(raw_event_text, nlp_spacy, nlp_stanza)
        text_fp = get_fp(raw_event_text, nlp_spacy)

        all_names.append(company_name)
        all_dates.append(text_date)
        all_times.append(text_time)
        all_fp.append(text_fp)

    save_to_csv(urls, all_names, all_dates, all_times, all_fp)


def extract_company(url, nlp_spacy, nlp_stanza):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    try:
        webpage = urlopen(req).read()
        mystr = webpage.decode("utf8")
        if mystr == None or len(mystr) < 1:
            return 'NONE'

        soup = BeautifulSoup(mystr, 'html5lib')

        title = soup.find('title')
        if title != None:
            title = re.sub("[(]\S+[)]", "", title.string)
            # print(title)  # Prints the tag string content

            spans = re.split("\B\W+\B", title)
            spans = [i for i in spans if i]

            company_name = ''

            for span in spans:
                # Augmented spacy
                # doc = nlp_spacy(span.strip().lower())
                # for ent in doc.ents:
                #     print('\t(Spacy)', ent.text, ':', ent.label_)

                # stanza (stanford ner)
                doc = nlp_stanza(span.strip())
                for ent in doc.entities:
                    # print(f'\t(stanza) {ent.text} : {ent.type}')
                    company_name = ent.text

            company_name = company_name.replace(",", "")
            return company_name

    except Exception as e:
        print('Error:', url)


def get_date_time(raw_event_text, nlp_spacy, nlp_stanza):
    # print('___________________________________')
    stanza_date = 'NONE'
    stanza_time = 'NONE'

    spacy_date = 'NONE'
    spacy_time = 'NONE'

    doc = nlp_spacy(raw_event_text)
    for ent in doc.ents:
        # print('\t(Spacy) <ENT>:', ent.text, '<Label>:', ent.label_)
        if ent.label_ == 'TIME':
            spacy_time = ent.text
        if ent.label_ == 'DATE':
            spacy_date = ent.text

    doc = nlp_stanza(raw_event_text)
    for ent in doc.entities:
        # print(f'\t(stanza) {ent.text}\t{ent.type}')
        if ent.type == 'TIME':
            stanza_time = ent.text
        if ent.type == 'DATE':
            stanza_date = ent.text

    return spacy_date, stanza_time


def get_fp(raw_event_text, nlp_spacy):
    # print('___________________________________')
    spacy_fp = 'NONE'

    doc = nlp_spacy(raw_event_text.lower())
    for ent in doc.ents:
        if ent.label_ == 'FISCAL_PERIOD':
            spacy_fp = ent.text

    return spacy_fp


def get_company(raw_event_text, nlp_spacy, nlp_stanza):
    # print('___________________________________')

    stanza_company = 'NONE'
    spacy_company = 'NONE'

    doc = nlp_spacy(raw_event_text)
    for ent in doc.ents:
        # print('\t(Spacy) <ENT>:', ent.text, '<Label>:', ent.label_)
        if ent.label_ == 'ORG':
            spacy_company = ent.text

    doc = nlp_stanza(raw_event_text)
    for ent in doc.entities:
        # print(f'\t(stanza) {ent.text}\t{ent.type}')
        if ent.type == 'ORG':
            stanza_company = ent.text

    return spacy_company


def save_to_csv(url_list, name_list, date_list, time_list, fp_list):
    # "{Company}, {Fiscal Year}, {Fiscal Period}, {Event Type}, {Event Date}, {Time}, {Timezone}"
    print('saving prediction')
    event1 = []
    event2 = []
    event3 = []
    event4 = []
    event5 = []
    blank = 'NONE'
    empty = 'EMPTY'
    for i in range(len(name_list)):
        event1.append(
            f'({name_list[i]}, {blank}, {fp_list[i]}, {blank}, {date_list[i]}, {time_list[i]}, {blank})')
        event2.append(empty)
        event3.append(empty)
        event4.append(empty)
        event5.append(empty)

    table = {'Link': url_list, '1': event1, '2': event2,
             '3': event3, '4': event4, '5': event5}
    df = pd.DataFrame(table)
    df.to_csv('predictions.csv', index=False)


if __name__ == '__main__':
    main()
