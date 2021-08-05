import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('configg.ini')

log_file = open('eval_comp.txt', 'w')

gold_file = config['pipeline']['INPUT_FILE']
et_model = config['pipeline']['event_type_model']

if et_model == 'bert':
    pred_file = config['pipeline']['bert_predictions']
elif et_model == 'gpt':
    pred_file = config['pipeline']['GPT_OUTPUT']
else:
    pred_file = config['pipeline']['REGEX_OUTPUT']

