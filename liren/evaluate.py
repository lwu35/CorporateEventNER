import pandas as pd
import os
from tqdm.auto import tqdm
from fuzzywuzzy import fuzz

file_path = os.path.join('60_links.csv')
df = pd.read_csv(file_path, sep=',', engine='python')
df = df.drop(df[df['Type'] == 'SKIPPED'].index)

gold_first = list(df['1'])

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

file_path = os.path.join('60_links.csv')
df = pd.read_csv(file_path, sep=',', engine='python')
pred_first = list(df['1'])

pred_company = []
pred_fiscal_year = []
pred_fiscal_period = []
pred_event_type = []
pred_date = []

pred_time = []
pred_timezone = []
pred_language = []
pred_phone_num = []
pred_webcast = []

for page in pred_first:
    # print(page)
    page = page[1:-1]
    event_info = page.split(',')

    pred_company.append(event_info[0].lower())
    pred_fiscal_year.append(event_info[1])
    pred_fiscal_period.append(event_info[2])
    pred_event_type.append(event_info[3].lower())
    pred_date.append(event_info[4])

    pred_time.append(event_info[5])
    pred_timezone.append(event_info[6])
    pred_language.append(event_info[7])
    pred_phone_num.append(event_info[8])
    pred_webcast.append(event_info[9])


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
    if pred_company[i] == gold_company[i]:
        count_company += 1

    if pred_fiscal_year[i] == gold_fiscal_year[i]:
        count_fiscal_year += 1

    if pred_fiscal_period[i] == gold_fiscal_period[i]:
        count_fiscal_period += 1

    if pred_event_type[i] == gold_event_type[i]:
        count_event_type += 1

    if pred_date[i] == gold_date[i]:
        count_date += 1

    if pred_time[i] == gold_time[i]:
        count_time += 1

    if pred_timezone[i] == gold_timezone[i]:
        count_timezone += 1

    if pred_language[i] == gold_language[i]:
        count_language += 1

    if pred_phone_num[i] == gold_phone_num[i]:
        count_phone_num += 1

    if pred_webcast[i] == gold_webcast[i]:
        count_webcast += 1

print('Company Acc:', count_company/len(gold_company))
print('Fiscal Year Acc:', count_fiscal_year/len(gold_company))
print('Fiscal Period Acc:', count_fiscal_period/len(gold_company))
print('Event Type Acc:', count_event_type/len(gold_company))
print('Date Acc:', count_date/len(gold_company))

print('Time Acc:', count_time/len(gold_company))
print('Timezone Acc:', count_timezone/len(gold_company))
print('Language Acc:', count_language/len(gold_company))
print('Phone Number Acc:', count_phone_num/len(gold_company))
print('Webcast URL Acc:', count_webcast/len(gold_company))

print(len(gold_company))


Str1 = "Kimberly-Clark Corporation"
Str2 = "Kimberly-Clark"

Partial_Ratio = fuzz.partial_ratio(Str1.lower(), Str2.lower())
Token_Set_Ratio = fuzz.token_set_ratio(Str1, Str2)

print(Partial_Ratio)
print(Token_Set_Ratio)
