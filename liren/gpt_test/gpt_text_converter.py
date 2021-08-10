import pandas as pd
import os
import re
import numpy as np


def space_checker(input_list):
    cleaned = []
    for line in input_list:
        cur = line.replace("\xa0", " ")
        cleaned.append(cur)
    return cleaned


'company,fiscal_year,fiscal_period,event_type,date,time,timezone'
'ASTRONICS,2021,Quarter 1/Q1,Earnings_Call,5/6/2021,11:00,EDT/EST/ET'

input_file_name = 'appen_train.csv'
output_file_name = 'gpt_train.txt'
tag = 'date'
version = 3
lower = False


def date_converter(date_type, str_date):
    if str(str_date) != 'NONE' and str(str_date) != 'none':
        months = {'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun',
                  '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
        if date_type == 'month':
            num = str_date.split('/')[0]
            return months[num]
        elif date_type == 'day':
            return str_date.split('/')[1]
    return 'NONE'


def write_file(input_file_name, output_file_name, tag, version, lower):
    file_path = os.path.join(input_file_name)
    df = pd.read_csv(file_path, sep=',', engine='python')
    event_texts = space_checker(list(df['event_text']))
    df = df.fillna('NONE')
    labels = list(df[tag])

    with open(output_file_name, 'w') as f:
        for i in range(len(event_texts)):
            event_text = event_texts[i].encode("ascii", "ignore")
            event_text = event_text.decode()
            event_text = event_text.strip()
            event_text = re.sub("\s\s+", " ", event_text)
            label = str(labels[i])

            label = label.encode("ascii", "ignore")
            label = label.decode()
            if lower:
                event_text = event_text.lower()
                label = label.lower()

            if version == 1:
                f.write(f'{event_text}.\n')
                f.write(f'The <{tag.upper()}> is {label}.\n')
            if version == 2:
                f.write(f'Text:{event_text}.\n')
                f.write(f'Type:{label}.\n')
                f.write(f'\n')
            if version == 3:
                f.write(f'{event_text}.\n')
                date_label = date_converter('month', label)
                f.write(f'The <MONTH> is {date_label}.\n')
    return 0


write_file(input_file_name, output_file_name, tag, version, lower)

input_file_name = 'appen_test.csv'
output_file_name = 'gpt_test.txt'

write_file(input_file_name, output_file_name, tag, version, lower)
