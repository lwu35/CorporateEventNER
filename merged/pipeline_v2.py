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

from gpt_neo import gpt_train, gpt_predict
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def main():
    file_path = os.path.join('job2_init.csv')
    df = pd.read_csv(file_path, sep=',', engine='python')

    event_ids = list(df['id'])
    event_texts = list(df['Event_Text'])
    urls = list(df['url'])
    url_ids = list(df['url_id'])

    nlp_spacy = spacy.load('en_core_web_lg')
    nlp_stanza = stanza.Pipeline('en', processors='tokenize,ner')

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
    all_types = []

    happy_gen = gpt_train('gpt_train.txt')

    for i in range(len(urls)):
        company_name = extract_company(urls[i], nlp_spacy, nlp_stanza)
        #company_name_2 = get_company(event_texts[i], nlp_spacy, nlp_stanza)
        text_date, text_time = get_date_time(
            event_texts[i], nlp_spacy, nlp_stanza)
        text_fp = get_fp(event_texts[i], nlp_spacy)
        event_type = gpt_predict(event_texts[i], happy_gen)

        all_names.append(company_name)
        all_dates.append(text_date)
        all_times.append(text_time)
        all_fp.append(text_fp)
        all_types.append(event_type)

    save_to_csv(urls, url_ids, event_ids, all_names,
                all_dates, all_times, all_fp, all_types)


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


def save_to_csv(url_list, url_ids, event_ids, name_list, date_list, time_list, fp_list, types_list):
    # "{Company}, {Fiscal Year}, {Fiscal Period}, {Event Type}, {Event Date}, {Time}, {Timezone}"
    print('saving prediction')
    event = []
    blank = 'NONE'

    for i in range(len(name_list)):
        event.append(
            f'({name_list[i]}, {blank}, {fp_list[i]}, {types_list}, {date_list[i]}, {time_list[i]}, {blank})')

    table = {'url': url_list, 'url_id': url_ids,
             'event_id': event_ids, 'event_info': event}
    df = pd.DataFrame(table)
    df.to_csv('predictions.csv', index=False)


if __name__ == '__main__':
    main()
