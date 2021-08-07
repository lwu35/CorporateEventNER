import csv
import pandas as pd

df = pd.read_csv('agg_86.csv')
#check appen quality

please_select_the_event_type_gold = df['please_select_the_event_type_gold'].tolist()

copy_the_company_name_from_the_text_gold = df['copy_the_company_name_from_the_text_gold'].astype(str).str.replace('\n', ' ').tolist()


select_the_fiscal_period_check_as_many_as_it_applies_gold= df['select_the_fiscal_period_check_as_many_as_it_applies_gold'].astype(str).str.replace('\n', ' ').tolist()


select_fiscal_year_gold = df['select_fiscal_year_gold'].tolist()

enter_date_here_mmddyyyy_gold = df['enter_date_here_mmddyyyy_gold'].tolist()

enter_time_here_hhmm_pmam_gold = df['enter_time_here_hhmm_pmam_gold'].astype(str).str.replace('\n', ' ').tolist()

select_timezone_gold = df['select_timezone_gold'].tolist()

please_select_the_event_type = df['please_select_the_event_type'].str.replace('_', ' ').tolist()

copy_the_company_name_from_the_text = df['copy_the_company_name_from_the_text'].astype(str).str.replace('\n', ' ').tolist()


select_the_fiscal_period_check_as_many_as_it_applies= df['select_the_fiscal_period_check_as_many_as_it_applies'].astype(str).str.replace('\n', ' ').str.replace('None/Other', 'NONE').str.replace('Quarter 1/Q1', 'Q1').str.replace('Quarter 2/Q2', 'Q2').str.replace('Quarter 3/Q3', 'Q3').str.replace('Quarter 4/Q4', 'Q4').str.replace('Annual/Yearly', 'Y').tolist()


select_fiscal_year = df['select_fiscal_year'].str.replace('\n', ' ').str.replace('None', 'NONE').tolist()

enter_date_here_mmddyyyy = df['enter_date_here_mmddyyyy'].tolist()

enter_time_here_hhmm_pmam = df['enter_time_here_hhmm_pmam'].astype(str).str.replace('nan', 'NONE').tolist()

select_timezone = df['select_timezone'].str.replace('None', 'NONE').str.replace('EDT/EST/ET', 'ET').str.replace('CDT/CST/CT', 'CDT').str.replace('MDT/MST/MT', 'MDT').str.replace('PDT/PST/PT', 'PDT').str.replace('Other', 'OTHER').tolist()

id = df['id'].tolist()

event_text = df['event_text'].tolist()

url = df['url'].tolist()

url_id= df['url_id'].tolist()

ids = []
nums = len(url_id)
for i in range(nums):
    ids.append(i+1)


#dict_gold = {'id': id, 'event_text': event_text, 'url': url, 'url_id': url_id, 'company': copy_the_company_name_from_the_text_gold, 'fiscal_year': select_fiscal_year_gold, 'fiscal_period': select_the_fiscal_period_check_as_many_as_it_applies_gold, 'event_type': please_select_the_event_type_gold, 'date': enter_date_here_mmddyyyy_gold, 'time': enter_time_here_hhmm_pmam_gold, 'timezone': select_timezone_gold}  
dict = {'id': ids, 'event_text': event_text, 'url': url, 'url_id': url_id, 'company': copy_the_company_name_from_the_text, 'fiscal_year': select_fiscal_year, 'fiscal_period': select_the_fiscal_period_check_as_many_as_it_applies, 'event_type': please_select_the_event_type, 'date': enter_date_here_mmddyyyy, 'time': enter_time_here_hhmm_pmam, 'timezone': select_timezone}  
df = pd.DataFrame(dict)

df.to_csv('cleaned_appen_86.csv')