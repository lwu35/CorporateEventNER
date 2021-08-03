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
'ASTRONICS,2021,Quarter 1/Q1,Earnings_Call,5/6/2021,11:00,EDT/EST/ET'

input_file_name = 'appen_train.csv'
output_file_name = 'gpt_train.txt'
tag = 'company'
version = 1
lower = False


def write_file(input_file_name, output_file_name, tag, version, lower):
    file_path = os.path.join(input_file_name)
    df = pd.read_csv(file_path, sep=',', engine='python')
    event_texts = space_checker(list(df['event_text']))
    labels = space_checker(list(df[tag]))

    with open(output_file_name, 'w') as f:
        for i in range(len(event_texts)):
            event_text = event_texts[i].encode("ascii", "ignore")
            event_text = event_text.decode()
            event_text = event_text.strip()
            event_text = re.sub("\s\s+", " ", event_text)
            label = labels[i].encode("ascii", "ignore")
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
    return 0


write_file(input_file_name, output_file_name, tag, version, lower)

input_file_name = 'appen_test.csv'
output_file_name = 'gpt_test.txt'

write_file(input_file_name, output_file_name, tag, version, lower)
