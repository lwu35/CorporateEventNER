import pandas as pd
import os
from tqdm.auto import tqdm
from fuzzywuzzy import fuzz

import datetime

from date_extractor import extract_dates
from dateparser.search import search_dates

NUM_EX = 20

file_path = os.path.join('60_links.csv')
df = pd.read_csv(file_path, sep=',', engine='python')
df = df.drop(df[df['Type'] == 'SKIPPED'].index)

gold_first = list(df['1'])[:NUM_EX]
print(f'Testing: {NUM_EX} examples')

gold_company = []
gold_fiscal_year = []
gold_fiscal_period = []
gold_event_type = []
gold_date = []

gold_time = []
gold_timezone = []
gold_language = []
gold_phone_num = []
gold_webcast = []

for page in gold_first:
    # print(page)
    page = page[1:-1]
    event_info = page.split(',')

    gold_company.append(event_info[0].lower())
    gold_fiscal_year.append(event_info[1])
    gold_fiscal_period.append(event_info[2])
    gold_event_type.append(event_info[3].lower())
    gold_date.append(event_info[4])

    gold_time.append(event_info[5])
    gold_timezone.append(event_info[6])
    gold_language.append(event_info[7])
    gold_phone_num.append(event_info[8])
    gold_webcast.append(event_info[9])

file_path = os.path.join('predictions.csv')
df = pd.read_csv(file_path, sep=',', engine='python')
df.company_name = df.company_name.fillna('-')
df.date = df.date.fillna('-')
df.time = df.time.fillna('-')

pred_company = list(df['company_name'])
pred_date = list(df['date'])
pred_time = list(df['time'])


pred_fiscal_year = []
pred_fiscal_period = []
pred_event_type = []

pred_timezone = []
pred_language = []
pred_phone_num = []
pred_webcast = []


count_company = 0
count_fiscal_year = 0
count_fiscal_period = 0
count_event_type = 0
count_date = 0

count_time = 0
count_timezone = 0
count_language = 0
count_phone_num = 0
count_webcast = 0


for i in range(len(gold_company)):
    # company comparison
    p_ratio = fuzz.partial_ratio(
        pred_company[i].lower(), gold_company[i].lower())
    ts_ratio = fuzz.token_set_ratio(pred_company[i], gold_company[i])
    if p_ratio >= .9 or ts_ratio >= .9:
        count_company += 1

    # if pred_fiscal_year[i] == gold_fiscal_year[i]:
    #     count_fiscal_year += 1

    # if pred_fiscal_period[i] == gold_fiscal_period[i]:
    #     count_fiscal_period += 1

    # if pred_event_type[i] == gold_event_type[i]:
    #     count_event_type += 1

    # date comparison
    cur_pred_date = '0'
    cur_gold_date = '1'
    if len(extract_dates(pred_date[i])) == 1:
        cur_pred_date = extract_dates(pred_date[i])[0].date()
    if len(extract_dates(gold_date[i])) == 1:
        cur_gold_date = extract_dates(gold_date[i])[0].date()
    if cur_pred_date == cur_gold_date:
        count_date += 1

    # time comparison
    gold_time[i] = gold_time[i].upper().replace('AM', 'A.M')
    gold_time[i] = gold_time[i].upper().replace('PM', 'P.M')
    pred_time[i] = pred_time[i].upper().replace('AM', 'A.M')
    pred_time[i] = pred_time[i].upper().replace('PM', 'P.M')

    cur_pred_time = '0'
    cur_gold_time = '1'
    if search_dates(gold_time[i]) != None:
        cur_gold_time = search_dates(gold_time[i])[0][1].time()
    if search_dates(pred_time[i]) != None:
        cur_pred_time = search_dates(pred_time[i])[0][1].time()
    if cur_pred_time == cur_gold_time:
        count_time += 1

    # if pred_timezone[i] == gold_timezone[i]:
    #     count_timezone += 1

    # if pred_language[i] == gold_language[i]:
    #     count_language += 1

    # if pred_phone_num[i] == gold_phone_num[i]:
    #     count_phone_num += 1

    # if pred_webcast[i] == gold_webcast[i]:
    #     count_webcast += 1

print('Company Acc:', count_company/len(gold_company))
# print('Fiscal Year Acc:', count_fiscal_year/len(gold_company))
# print('Fiscal Period Acc:', count_fiscal_period/len(gold_company))
# print('Event Type Acc:', count_event_type/len(gold_company))
print('Date Acc:', count_date/len(gold_company))

print('Time Acc:', count_time/len(gold_company))
# print('Timezone Acc:', count_timezone/len(gold_company))
# print('Language Acc:', count_language/len(gold_company))
# print('Phone Number Acc:', count_phone_num/len(gold_company))
# print('Webcast URL Acc:', count_webcast/len(gold_company))


# Str1 = "Kimberly-Clark Corporation"
# Str2 = "Kimberly-Clark"

# Partial_Ratio = fuzz.partial_ratio(Str1.lower(), Str2.lower())
# Token_Set_Ratio = fuzz.token_set_ratio(Str1, Str2)

# print(Partial_Ratio)
# print(Token_Set_Ratio)
