import pandas as pd
import os
import re


def space_checker(input_list):
    cleaned = []
    for line in input_list:
        cur = line.replace("\xa0", " ")
        cleaned.append(cur)
    return cleaned


'company,fiscal_year,fiscal_period,event_type,date,time,timezone'
tag = 'time'
version = 1

file_path = os.path.join('job2_gold.csv')
df = pd.read_csv(file_path, sep=',', engine='python')
event_texts = space_checker(list(df['event_text']))
labels = space_checker(list(df[tag]))

with open('gpt_train.txt', 'w') as f:
    for i in range(len(event_texts)):
        event_text = event_texts[i].strip()
        event_text = re.sub("\s\s+", " ", event_text)
        if version == 1:
            f.write(f'{event_text}.\n')
            f.write(f'The <{tag.upper()}> is {labels[i]}.\n')
        if version == 2:
            f.write(f'Text:{event_text}.\n')
            f.write(f'Type:{labels[i]}.\n')
            f.write(f'\n')
