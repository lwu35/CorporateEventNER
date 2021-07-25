import pandas as pd
import os
from tqdm.auto import tqdm

import spacy
from spacy.pipeline import EntityRuler
import stanza

import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from gpt_neo import gpt_predict
from bert_event_type import bert_predict
from happytransformer import HappyGeneration

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def main():
    file_path = os.path.join('job2_gold.csv')
    df = pd.read_csv(file_path, sep=',', engine='python')

    event_ids = list(df['id'])
    event_texts = list(df['event_text'])
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
               "full year", "annual", "first half", "second half"]
    for item in periods:
        ruler.add_patterns([{"label": "FISCAL_PERIOD", "pattern": item}])

    # add custom rules to the pipe
    nlp_spacy.add_pipe(ruler)
    all_names = []
    all_dates = []
    all_times = []
    all_fy = []
    all_fp = []
    all_types_bert = []
    all_types_gpt = []
    all_timezones = []

    # doc = nlp_spacy(
    #     'the event takes place in the third quarter. Or was it in quarter 1. Or q2. Oct 25, 2021 at 9:00 AM CDT Third Quarter 2021 Earnings')
    # for ent in doc.ents:
    #     print('\t(Spacy) <ENT>:', ent.text, '<Label>:', ent.label_)

    # GPT-NEO Model, event type
    happy_gen = HappyGeneration(load_path="model-gpt/")

    for i in range(len(urls)):
        # print(event_texts[i])
        company_name = extract_company(urls[i], nlp_spacy, nlp_stanza)
        # company_name_2 = get_company(event_texts[i], nlp_spacy, nlp_stanza)
        text_date, text_time, text_timezone = get_date_time(
            event_texts[i], nlp_spacy, nlp_stanza)
        if text_timezone == 'NONE':
            text_timezone = get_timezone(event_texts[i])
        text_fp = get_fp(event_texts[i], nlp_spacy)
        event_type_gpt = gpt_predict(event_texts[i], happy_gen)
        event_type_bert = bert_predict(event_texts[i])

        all_names.append(company_name)
        all_fy.append('NONE')
        all_fp.append(text_fp)
        all_dates.append(text_date)
        all_times.append(text_time)
        all_timezones.append(text_timezone)
        all_types_bert.append(event_type_bert)
        all_types_gpt.append(event_type_gpt)

    save_to_csv('gpt_predictions.csv', event_ids, event_texts, urls, url_ids, all_names, all_fy, all_fp, all_types_gpt,
                all_dates, all_times, all_timezones)

    save_to_csv('bert_predictions.csv', event_ids, event_texts, urls, url_ids, all_names, all_fy, all_fp, all_types_bert,
                all_dates, all_times, all_timezones)


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

            company_name = 'NONE'

            for span in spans:
                # Augmented spacy
                # doc = nlp_spacy(span.strip().lower())
                # for ent in doc.ents:
                #     # print('\t(Spacy)', ent.text, ':', ent.label_)
                #     if ent.label_ == 'ORG':
                #         company_name = ent.text

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
    stanza_date = []
    stanza_time = []
    stanza_timezone = 'NONE'

    spacy_date = []
    spacy_time = []

    doc = nlp_spacy(raw_event_text)
    for ent in doc.ents:
        # print('\t(Spacy) <ENT>:', ent.text, '<Label>:', ent.label_)
        if ent.label_ == 'TIME':
            spacy_time.append(ent.text)
        if ent.label_ == 'DATE':
            spacy_date.append(ent.text)

    doc = nlp_stanza(raw_event_text)
    for ent in doc.entities:
        # print(f'\t(stanza) {ent.text}\t{ent.type}')
        if ent.type == 'TIME':
            stanza_time.append(ent.text)
            stanza_timezone = time_zone_finder(
                ent.text.lower()).strip()
            # print(stanza_timezone)

        if ent.type == 'DATE':
            stanza_date.append(ent.text)

    if len(stanza_time) == 0:
        stanza_time.append('NONE')
    if len(stanza_date) == 0:
        stanza_date.append('NONE')
    if len(stanza_timezone) == 0:
        stanza_timezone = 'NONE'

    return best_date(stanza_date), strip_time_zone(stanza_time[0].lower()), stanza_timezone


def get_fp(raw_event_text, nlp_spacy):
    spacy_fp = 'NONE'

    doc = nlp_spacy(raw_event_text.lower())
    for ent in doc.ents:
        if ent.label_ == 'FISCAL_PERIOD':
            spacy_fp = ent.text

    return spacy_fp.upper()


def get_timezone(raw_event_text):
    regex_timezone = 'NONE'

    timezones = ['pst', 'pt', 'pdt', 'est', 'et',
                 'edt', 'ct', 'cst', 'cdt', 'mt', 'mdt', 'mst']
    for zone in timezones:
        for word in raw_event_text.lower().split():
            if zone == word:
                regex_timezone = zone

    return regex_timezone.upper()


def get_company(raw_event_text, nlp_spacy, nlp_stanza):
    # print('___________________________________')

    stanza_company = 'NONE'
    spacy_company = 'NONE'

    doc = nlp_spacy(raw_event_text)
    for ent in doc.ents:
        # print('\t(Spacy) <ENT>:', ent.text, '<Label>:', ent.label_)
        if ent.label_ == 'ORG':
            spacy_company = ent.text

    # doc = nlp_stanza(raw_event_text)
    # for ent in doc.entities:
    #     # print(f'\t(stanza) {ent.text}\t{ent.type}')
    #     if ent.type == 'ORG':
    #         stanza_company = ent.text

    return spacy_company


def best_date(date_list):
    if len(date_list) == 1:
        return date_list[0]
    else:
        for i in date_list:
            if len(i.split()) > 1:
                return i
        return date_list[0]


def time_zone_finder(time_text):
    patterns = ['am', 'pm', 'a.m', 'p.m']
    found = ''
    for p in patterns:
        if p in time_text:
            found += time_text.split(p)[1]
    return found.upper()


def strip_time_zone(time_text):
    patterns = ['am', 'pm', 'a.m', 'p.m']
    found = 'NONE'
    for p in patterns:
        if p in time_text:
            found = time_text.split(p)[0] + p
    return found.upper()


def save_to_csv(file_name, event_ids, event_texts, url_list, url_ids, name_list, fy_list, fp_list, types_list, date_list, time_list, timezone_list):
    # id,event_text,url,url_id,company,fiscal_year,fiscal_period,event_type,date,time,timezone"
    print('saving prediction:', file_name)

    table = {'id': event_ids, 'event_text': event_texts, 'url': url_list, 'url_id': url_ids, 'company': name_list, 'fiscal_year': fy_list,
             'fiscal_period': fp_list, 'event_type': types_list, 'date': date_list, 'time': time_list, 'timezone': timezone_list}
    df = pd.DataFrame(table)
    df.to_csv(file_name, index=False)


if __name__ == '__main__':
    main()
