import csv
import pandas as pd
from datetime import datetime
d = datetime.strptime("10:30", "%H:%M")
d.strftime("%I:%M %p")


def date_converter(str_date):

    months = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr', '5': 'May', '6': 'Jun', 
              '7': 'Jul', '8': 'Aug', '9': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
    if str(str_date) != 'NONE':
        parse = str_date.split('/')
        return f"{months[parse[0]]} {parse[1]}, {parse[2]}"

    return 'NONE'


def time_converter(str_time):
    if str_time != 'NONE':
        d = datetime.strptime(str_time, "%H:%M")
        return d.strftime("%I:%M %p")

    return 'NONE'


df = pd.read_csv('appen812edits.csv')
# check appen quality
df = df.fillna('NONE')

please_select_the_event_type_gold = df['please_select_the_event_type_gold'].tolist(
)

copy_the_company_name_from_the_text_gold = df['copy_the_company_name_from_the_text_gold'].astype(
    str).str.replace('\n', ' ').tolist()


select_the_fiscal_period_check_as_many_as_it_applies_gold = df['select_the_fiscal_period_check_as_many_as_it_applies_gold'].astype(
    str).str.replace('\n', ' ').tolist()


select_fiscal_year_gold = df['select_fiscal_year_gold'].tolist()

enter_date_here_mmddyyyy_gold = df['enter_date_here_mmddyyyy_gold'].tolist()

enter_time_here_hhmm_pmam_gold = df['enter_time_here_hhmm_pmam_gold'].astype(
    str).str.replace('\n', ' ').tolist()

select_timezone_gold = df['select_timezone_gold'].tolist()

please_select_the_event_type = df['please_select_the_event_type'].str.replace(
    '_', ' ').tolist()

copy_the_company_name_from_the_text = df['copy_the_company_name_from_the_text'].astype(
    str).str.replace('\n', ' ').tolist()


select_the_fiscal_period_check_as_many_as_it_applies = df['select_the_fiscal_period_check_as_many_as_it_applies'].astype(str).str.replace('\n', ' ').str.replace(
    'None/Other', 'NONE').str.replace('Quarter 1/Q1', 'Q1').str.replace('Quarter 2/Q2', 'Q2').str.replace('Quarter 3/Q3', 'Q3').str.replace('Quarter 4/Q4', 'Q4').str.replace('Annual/Yearly', 'Y').tolist()


select_fiscal_year = df['select_fiscal_year'].str.replace(
    '\n', ' ').str.replace('None', 'NONE').tolist()

enter_date_here_mmddyyyy = df['enter_date_here_mmddyyyy'].tolist()
converted_date = []
for date_obj in enter_date_here_mmddyyyy:
    converted_date.append(date_converter(str(date_obj)))

converted_time = []
enter_time_here_hhmm_pmam = df['enter_time_here_hhmm_pmam'].astype(
    str).str.replace('nan', 'NONE').tolist()
for time_obj in enter_time_here_hhmm_pmam:
    converted_time.append(time_converter(str(time_obj)))


select_timezone = df['select_timezone'].str.replace('None', 'NONE').str.replace('EDT/EST/ET', 'ET').str.replace(
    'CDT/CST/CT', 'CDT').str.replace('MDT/MST/MT', 'MDT').str.replace('PDT/PST/PT', 'PDT').str.replace('Other', 'OTHER').tolist()

id = df['id'].tolist()

event_text = df['event_text'].tolist()

url = df['url'].tolist()

url_id = df['url_id'].tolist()

ids = []
nums = len(url_id)
for i in range(nums):
    ids.append(i+1)


#dict_gold = {'id': id, 'event_text': event_text, 'url': url, 'url_id': url_id, 'company': copy_the_company_name_from_the_text_gold, 'fiscal_year': select_fiscal_year_gold, 'fiscal_period': select_the_fiscal_period_check_as_many_as_it_applies_gold, 'event_type': please_select_the_event_type_gold, 'date': enter_date_here_mmddyyyy_gold, 'time': enter_time_here_hhmm_pmam_gold, 'timezone': select_timezone_gold}
dict = {'id': ids, 'event_text': event_text, 'url': url, 'url_id': url_id, 'company': copy_the_company_name_from_the_text, 'fiscal_year': select_fiscal_year,
        'fiscal_period': select_the_fiscal_period_check_as_many_as_it_applies, 'event_type': please_select_the_event_type, 'date': converted_date, 'time': converted_time, 'timezone': select_timezone}
df = pd.DataFrame(dict)

df.to_csv('cleaned_appen_812.csv', index=False)
