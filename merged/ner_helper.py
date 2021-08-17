import pandas as pd
import os

import spacy
from spacy.pipeline import EntityRuler

from allennlp.predictors.predictor import Predictor

from simpletransformers.question_answering import QuestionAnsweringModel

import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def init_allen_nlp():
    predictor = Predictor.from_path(
        "https://storage.googleapis.com/allennlp-public-models/transformer-qa.2021-02-11.tar.gz")
    return predictor


def roberta_company(model, event_text):

    example = [
        {
            "context": event_text,
            "qas": [
                {
                    "question": "What is the company?",
                    "id": "0",
                }
            ],
        }
    ]

    answers, probabilities = model.predict(example)

    name = answers[0]['answer'][0]

    if name == '' or name == 'empty':
        return 'NONE'

    return name


def allen_company(model, event_text, event_type='default'):

    if event_type == 'Conference':
        name = model.predict(passage=event_text, question="What company is hosting the conference?")[
            'best_span_str']
    else:
        name = model.predict(passage=event_text, question="What is the company?")[
            'best_span_str']

    if name == '':
        return 'NONE'
    return name


def allen_date(model, event_text):
    date = model.predict(passage=event_text, question="What is the date?")[
        'best_span_str']

    if date == '':
        return 'NONE'
    return date


def allen_time(model, event_text):
    time = model.predict(passage=event_text, question="What is the event time?")[
        'best_span_str']

    if time == '':
        return 'NONE'
    return strip_time_zone(time.lower())


def allen_timezone(model, event_text):
    timezone = model.predict(passage=event_text, question="What is the time zone?")[
        'best_span_str']

    if timezone == '':
        return 'NONE'
    return timezone


def spacy_init(base_model):
    nlp_spacy = spacy.load(base_model)

    # add custom entity to spacy
    ruler = EntityRuler(nlp_spacy, overwrite_ents=True)

    # # load companies list
    # file_path = os.path.join('company_names_nasdaq.csv')
    # df = pd.read_csv(file_path, sep=',', engine='python')
    # companies = list(df['name'])

    # # tag companies
    # for item in companies:
    #     ruler.add_patterns([{"label": "ORG", "pattern": item}])

    # tag periods
    periods = ["q1", "q2", "q3", "q4",
               "1q", "2q", "3q", "4q",
               "quarter 1", "quarter 2", "quarter 3", "quarter 4",
               "1st quarter", "2nd quarter", "3rd quarter", "4th quarter",
               "first quarter", "second quarter", "third quarter", "fourth quarter",
               "full year", "annual", "first half", "second half"]
    for item in periods:
        ruler.add_patterns([{"label": "FISCAL_PERIOD", "pattern": item}])

    # add custom rules to the pipe
    nlp_spacy.add_pipe(ruler)

    return nlp_spacy


def extract_company(url, nlp_stanza):
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
                # stanza (stanford ner)
                doc = nlp_stanza(span.strip())
                for ent in doc.entities:
                    company_name = ent.text

            company_name = company_name.replace(",", "")
            return company_name

    except:
        return 'NONE'


def get_date_time_timezone(raw_event_text, nlp_stanza):
    stanza_date = []
    stanza_time = []
    stanza_timezone = 'NONE'

    doc = nlp_stanza(raw_event_text)
    for ent in doc.entities:
        if ent.type == 'TIME':
            stanza_time.append(ent.text)

            stanza_timezone = time_zone_finder(
                ent.text.lower()).strip()

        if ent.type == 'DATE':
            stanza_date.append(ent.text)

    if len(stanza_time) == 0:
        stanza_time.append('NONE')
    if len(stanza_date) == 0:
        stanza_date.append('NONE')
    if len(stanza_timezone) == 0:
        stanza_timezone = get_timezone(raw_event_text)

    return best_date(stanza_date), strip_time_zone(stanza_time[0].lower()), stanza_timezone


def get_fp(raw_event_text, nlp_spacy):
    spacy_fp = 'NONE'
    doc = nlp_spacy(raw_event_text.lower())
    for ent in doc.ents:
        if ent.label_ == 'FISCAL_PERIOD':
            spacy_fp = ent.text

    return spacy_fp.upper()


def get_fp_regex(raw_event_text):
    raw_event_text = raw_event_text.lower()
    if 'q1' in raw_event_text or 'first quarter' in raw_event_text or '1q' in raw_event_text or '1q21' in raw_event_text or '1q20' in raw_event_text or 'q121' in raw_event_text or 'q120' in raw_event_text or 'first-quarter' in raw_event_text or '1st quarter' in raw_event_text or '2021q1' in raw_event_text or '2020q1' in raw_event_text or '2019q1' in raw_event_text:
        return 'Q1'
    elif '3q20' in raw_event_text or '3q21' in raw_event_text:
        return 'Q3'
    elif '4q20' in raw_event_text or '4q21' in raw_event_text:
        return 'Q4'
    elif 'q2' in raw_event_text or 'second quarter' in raw_event_text or '2q' in raw_event_text or '2q21' in raw_event_text or '2q20' in raw_event_text or 'q221' in raw_event_text or 'q220' in raw_event_text or 'second-quarter' in raw_event_text or '2nd quarter' in raw_event_text or '2021q2' in raw_event_text or '2020q2' in raw_event_text or '2019q2' in raw_event_text:
        return 'Q2'
    elif 'q3' in raw_event_text or 'third quarter' in raw_event_text or '3q' in raw_event_text or '3q21' in raw_event_text or '3q20' in raw_event_text or 'q321' in raw_event_text or 'q220' in raw_event_text or 'third-quarter' in raw_event_text or '3rd quarter' in raw_event_text or '2021q3' in raw_event_text or '2020q3' in raw_event_text or '2019q3' in raw_event_text:
        return 'Q3'
    elif 'q4' in raw_event_text or 'fourth quarter' in raw_event_text or '4q' in raw_event_text or '4q21' in raw_event_text or '4q20' in raw_event_text or 'q421' in raw_event_text or 'q220' in raw_event_text or 'fourth-quarter' in raw_event_text or '4th quarter' in raw_event_text or '2021q4' in raw_event_text or '2020q4' in raw_event_text or '2019q4' in raw_event_text:
        return 'Q4'
    elif 'annual' in raw_event_text or 'yearly' in raw_event_text or 'full year' in raw_event_text or 'annually' in raw_event_text or 'yearly' in raw_event_text:
        return 'Y'
    elif 'first half' in raw_event_text:
        return 'S1'
    elif 'second half' in raw_event_text:
        return 'S2'
    else:
        return 'NONE'


def get_fy(raw_event_text, text_date):
    fy = ['2017', '2018', '2019', '2020', '2021', '2022']
    raw_event_text = raw_event_text.replace(text_date, '')
    for token in raw_event_text.split():
        if token in fy:
            return token
    return 'NONE'


def get_timezone(raw_event_text):
    regex_timezone = 'NONE'
    timezones = ['pst', 'pt', 'pdt', 'est', 'et',
                 'edt', 'ct', 'cst', 'cdt', 'mt', 'mdt', 'mst']
    for zone in timezones:
        for word in raw_event_text.lower().split():
            if zone == word:
                regex_timezone = zone

    return regex_timezone.upper()


def get_company(raw_event_text, nlp_spacy, nlp_stanza, used_tokens):
    stanza_company = 'NONE'
    spacy_company = 'NONE'
    for span in used_tokens:
        raw_event_text = raw_event_text.replace(span, '')
    print(raw_event_text)
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

    return stanza_company


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
    for p in patterns:
        if p in time_text:
            return time_text.split(p)[1].upper()
    return ''


def strip_time_zone(time_text):
    patterns = ['am', 'pm', 'a.m', 'p.m']
    for p in patterns:
        if p in time_text:
            found = time_text.split(p)[0] + p
            return found.upper()
    return 'NONE'


def get_regex_event_type(sent):
    if 'merger' in sent or 'acquisition' in sent:
        return 'Merger/Acquisition'
    elif ('earnings' in sent or ('financial' in sent and 'results' in sent)) and ('call' in sent or 'calls' in sent):
        return 'Earnings Call'
    elif 'earnings' in sent or ('financial' in sent and 'results' in sent):
        return 'Earnings Release'
    elif 'stockholders' in sent or 'shareholders' in sent or 'investor' in sent or 'shareholder' in sent:
        return 'Shareholder Meeting'
    elif 'conference' in sent and 'earnings' not in sent or 'summit' in sent:
        return 'Conference'
    elif 'guidance' in sent:
        return 'Guidance'
    else:
        return 'None/Other'
