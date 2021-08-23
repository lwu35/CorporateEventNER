import configparser
import os
import stanza

import tkinter as tk
from tkinter import ttk

from gpt_neo import gpt_predict
from bert_event_type import bert_predict, bert_init
from happytransformer import HappyGeneration
from allennlp.predictors.predictor import Predictor

from simpletransformers.question_answering import QuestionAnsweringModel

from ner_helper import get_date_time_timezone, get_fp, get_fp_regex, get_fy, spacy_init, get_regex_event_type, init_allen_nlp, allen_company, allen_date, allen_time, allen_timezone, roberta_company, get_company
from ner_normalize import normalize_date, normalize_time, normalize_fiscal_period, timezone_converter


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


def init_models():
    # nlp_spacy = spacy_init('en_core_web_lg')
    # stanza.download('en')
    nlp_stanza = stanza.Pipeline('en', processors='tokenize,ner')
    nlp_allen = Predictor.from_path(
        "https://storage.googleapis.com/allennlp-public-models/transformer-qa.2021-02-11.tar.gz")
    roberta_qa = QuestionAnsweringModel("roberta", "model-roberta")

    # GPT-NEO Model, event type
    gpt_model = HappyGeneration(load_path=GPT_MODEL_PATH_EVENT_TYPE)

    # BERT Model, event type
    bert_model, intent2id, id2intent, tokenizer = bert_init(
        dropout_value=BERT_DROPOUT, saved_model=BERT_MODEL_PATH_EVENT_TYPE)

    return nlp_stanza, nlp_allen, roberta_qa, gpt_model, bert_model, intent2id, id2intent, tokenizer


def main():
    print('--------------------------Init Models-------------------------')
    nlp_stanza, nlp_allen, roberta_qa, gpt_model, bert_model, intent2id, id2intent, tokenizer = init_models()

    label_font_size = 18
    text_font_size = 12
    print('--------------------------Running window-------------------------')
    root = tk.Tk()
    root.title('Corporate Event Extraction')

    canvas = tk.Canvas(root, width=600, height=500)
    canvas.grid(columnspan=5, rowspan=10)

    entry = tk.Entry(root, width=80, borderwidth=4, font=("Calibri 12"))
    entry.grid(columnspan=5, column=0, row=1, padx=20, pady=10)
    entry.focus()

    instructions = tk.Label(
        root, text='Enter event text to extract entities:'.upper(), font=("Consolas", 20))
    instructions.grid(columnspan=5, column=0, row=0, padx=10, pady=10)

    company = tk.Label(
        root, text='Company: ', font=('Consolas', label_font_size))
    fy = tk.Label(
        root, text='Fiscal year: ', font=("Consolas", label_font_size))
    fp = tk.Label(
        root, text='Fiscal period: ', font=("Consolas", label_font_size))
    et = tk.Label(
        root, text='Event type: ', font=("Consolas", label_font_size))
    date = tk.Label(
        root, text='Date: ', font=("Consolas", label_font_size))
    time = tk.Label(
        root, text='Time: ', font=("Consolas", label_font_size))
    tz = tk.Label(
        root, text='Time zone: ', font=("Consolas", label_font_size))

    company.grid(column=0, row=4, padx=10,)
    fy.grid(column=0, row=5, padx=10,)
    fp.grid(column=0, row=6, padx=10,)
    et.grid(column=0, row=7, padx=10,)
    date.grid(column=0, row=8, padx=10,)
    time.grid(column=0, row=9, padx=10,)
    tz.grid(column=0, row=10, padx=10,)

    result_company = tk.Text(root, height=1, width=35,
                             padx=10, pady=10, font=("Courier", text_font_size))
    result_fy = tk.Text(root, height=1, width=35, padx=10,
                        pady=10, font=("Courier", text_font_size))
    result_fp = tk.Text(root, height=1, width=35, padx=10,
                        pady=10, font=("Courier", text_font_size))
    result_et = tk.Text(root, height=1, width=35, padx=10,
                        pady=10, font=("Courier", text_font_size))
    result_date = tk.Text(root, height=1, width=35,
                          padx=10, pady=10, font=("Courier", text_font_size))
    result_time = tk.Text(root, height=1, width=35,
                          padx=10, pady=10, font=("Courier", text_font_size))
    result_tz = tk.Text(root, height=1, width=35, padx=10,
                        pady=10, font=("Courier", text_font_size))

    result_company.grid(column=2, row=4)
    result_fy.grid(column=2, row=5)
    result_fp.grid(column=2, row=6)
    result_et.grid(column=2, row=7)
    result_date.grid(column=2, row=8)
    result_time.grid(column=2, row=9)
    result_tz.grid(column=2, row=10)

    def pipeline(nlp_stanza, nlp_allen, roberta_qa, gpt_model, bert_model, intent2id, id2intent, tokenizer):
        input_text = entry.get()
        try:
            text_date, text_time, text_timezone = get_date_time_timezone(
                input_text, nlp_stanza)
        except:
            text_date, text_time, text_timezone = 'NONE'

        try:
            text_date = allen_date(nlp_allen, input_text)
        except:
            text_date = 'NONE'

        try:
            text_time = allen_time(nlp_allen, input_text)
        except:
            text_time = 'NONE'

        try:
            # text_fp = get_fp(event_texts[i], nlp_spacy)
            text_fp = get_fp_regex(input_text)
        except:
            text_fp = 'NONE'

        try:
            event_type_gpt = gpt_predict(input_text, gpt_model)
        except:
            event_type_gpt = 'NONE'

        try:
            event_type_bert = bert_predict(
                input_text, bert_model, intent2id, id2intent, tokenizer)
        except:
            event_type_bert = 'NONE'

        try:
            event_type_regex = get_regex_event_type(input_text.lower())
        except:
            event_type_regex = 'NONE'

        try:
            text_fy = get_fy(input_text, text_date)
        except:
            text_fy = 'NONE'

        # try:
        #     company_name = allen_company(nlp_allen, event_texts[i])
        # except:
        #     company_name = 'NONE'

        try:
            company_name = roberta_company(roberta_qa, input_text)
        except:
            company_name = 'NONE'
        # company_name = get_company(event_texts[i], nlp_spacy, nlp_stanza)

        result_company.delete("1.0", "end")
        result_fy.delete("1.0", "end")
        result_fp.delete("1.0", "end")
        result_et.delete("1.0", "end")
        result_date.delete("1.0", "end")
        result_time.delete("1.0", "end")
        result_tz.delete("1.0", "end")

        result_company.insert(1.0, company_name)
        result_fy.insert(1.0, text_fy)
        result_fp.insert(1.0, normalize_fiscal_period(text_fp))
        result_et.insert(1.0, event_type_bert)
        result_date.insert(1.0, normalize_date(text_date))
        result_time.insert(1.0, normalize_time(text_time))
        result_tz.insert(1.0, timezone_converter(text_timezone))

    def test():
        result_company.delete("1.0", "end")
        s = entry.get()
        result_company.insert(1.0, s)

    separator = ttk.Separator(root, orient='horizontal')
    separator.grid(columnspan=5, row=3, sticky='ew')

    button = tk.Button(root, text='Extract text'.upper(), font=("Consolas", 18, 'bold'), bg='#5DADE2', fg='white', height=2, width=18,
                       command=lambda: pipeline(nlp_stanza, nlp_allen, roberta_qa, gpt_model, bert_model, intent2id, id2intent, tokenizer))

    # button = tk.Button(root, text='Extract text',
    #                    command=test, font=("Raleway", 16), bg='#5DADE2', fg='white', height=2, width=20)
    button.grid(columnspan=5, row=2)

    canvas = tk.Canvas(root, width=600, height=50)
    canvas.grid(columnspan=5)

    root.mainloop()


if __name__ == '__main__':
    main()
