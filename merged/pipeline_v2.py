import pandas as pd
import os
import configparser
import stanza

from gpt_neo import gpt_predict
from bert_event_type import bert_predict, bert_init
from happytransformer import HappyGeneration

from ner_helper import get_date_time_timezone, get_fp, get_fy, extract_company, get_company, spacy_init, get_regex_event_type

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


config = configparser.ConfigParser()
config.read('configg.ini')


INPUT_FILE = config['pipeline']['INPUT_FILE']

BERT_MODEL_PATH_EVENT_TYPE = config['pipeline']['model_path_bert']
dropout = config['bert_model']['dropout']
dropout = float(dropout)
BERT_DROPOUT = dropout
BERT_OUTPUT = config['pipeline']['bert_predictions']

GPT_MODEL_PATH_EVENT_TYPE = config['pipeline']['GPT_MODEL_PATH_EVENT_TYPE']
GPT_OUTPUT = config['pipeline']['GPT_OUTPUT']

REGEX_OUTPUT = config['pipeline']['REGEX_OUTPUT']


def main():
    file_path = os.path.join(INPUT_FILE)
    df = pd.read_csv(file_path, sep=',', engine='python')

    event_ids = list(df['id'])
    event_texts = list(df['event_text'])
    urls = list(df['url'])
    url_ids = list(df['url_id'])

    nlp_spacy = spacy_init('en_core_web_lg')
    nlp_stanza = stanza.Pipeline('en', processors='tokenize,ner')

    # GPT-NEO Model, event type
    happy_gen = HappyGeneration(load_path=GPT_MODEL_PATH_EVENT_TYPE)

    # BERT Model, event type
    model, intent2id, id2intent, tokenizer = bert_init(
        dropout_value=BERT_DROPOUT, saved_model=BERT_MODEL_PATH_EVENT_TYPE)

    all_names = []
    all_dates = []
    all_times = []
    all_fy = []
    all_fp = []
    all_types_bert = []
    all_types_gpt = []
    all_types_regex = []
    all_timezones = []

    for i in range(len(urls)):
        # print(event_texts[i])
        company_name = extract_company(urls[i], nlp_stanza)
        # company_name = get_company(event_texts[i], nlp_spacy, nlp_stanza)
        text_date, text_time, text_timezone = get_date_time_timezone(
            event_texts[i], nlp_stanza)

        text_fp = get_fp(event_texts[i], nlp_spacy)

        event_type_gpt = gpt_predict(event_texts[i], happy_gen)

        event_type_bert = bert_predict(
            event_texts[i], model, intent2id, id2intent, tokenizer)

        event_type_regex = get_regex_event_type(event_texts[i])

        text_fy = get_fy(event_texts[i], text_date)

        all_names.append(company_name)
        all_fy.append(text_fy)
        all_fp.append(text_fp)
        all_dates.append(text_date)
        all_times.append(text_time)
        all_timezones.append(text_timezone)
        all_types_bert.append(event_type_bert)
        all_types_gpt.append(event_type_gpt)
        all_types_regex.append(event_type_regex)

    save_to_csv(GPT_OUTPUT, event_ids, event_texts, urls, url_ids, all_names, all_fy, all_fp, all_types_gpt,
                all_dates, all_times, all_timezones)
    save_to_csv(BERT_OUTPUT, event_ids, event_texts, urls, url_ids, all_names, all_fy, all_fp, all_types_bert,
                all_dates, all_times, all_timezones)
    save_to_csv(REGEX_OUTPUT, event_ids, event_texts, urls, url_ids,
                all_names, all_fy, all_fp, all_types_regex, all_dates, all_times, all_timezones)


def save_to_csv(file_name, event_ids, event_texts, url_list, url_ids, name_list, fy_list, fp_list, types_list, date_list, time_list, timezone_list):
    # id,event_text,url,url_id,company,fiscal_year,fiscal_period,event_type,date,time,timezone"
    print('Saving prediction:', file_name)

    table = {'id': event_ids, 'event_text': event_texts, 'url': url_list, 'url_id': url_ids, 'company': name_list, 'fiscal_year': fy_list,
             'fiscal_period': fp_list, 'event_type': types_list, 'date': date_list, 'time': time_list, 'timezone': timezone_list}
    df = pd.DataFrame(table)
    df.to_csv(file_name, index=False)


if __name__ == '__main__':
    main()
