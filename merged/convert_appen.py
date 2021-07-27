import csv
import pandas as pd

df = pd.read_csv('appen_test.csv')


please_select_the_event_type_gold = df['please_select_the_event_type_gold'].tolist()

copy_the_company_name_from_the_text_gold = df['copy_the_company_name_from_the_text_gold'].astype(str).str.replace('\n', ' ').tolist()


select_the_fiscal_period_check_as_many_as_it_applies_gold= df['select_the_fiscal_period_check_as_many_as_it_applies_gold'].astype(str).str.replace('\n', ' ').tolist()


select_fiscal_year_gold = df['select_fiscal_year_gold'].tolist()

enter_date_here_mmddyyyy_gold = df['enter_date_here_mmddyyyy_gold'].tolist()

enter_time_here_hhmm_pmam_gold = df['enter_time_here_hhmm_pmam_gold'].astype(str).str.replace('\n', ' ').tolist()

select_timezone_gold = df['select_timezone_gold'].tolist()

please_select_the_event_type = df['_please_select_the_event_type'].tolist()

copy_the_company_name_from_the_text = df['_copy_the_company_name_from_the_text'].astype(str).str.replace('\n', ' ').tolist()


select_the_fiscal_period_check_as_many_as_it_applies= df['_select_the_fiscal_period_check_as_many_as_it_applies'].astype(str).str.replace('\n', ' ').tolist()


select_fiscal_year = df['_select_fiscal_year'].tolist()

enter_date_here_mmddyyyy = df['_enter_date_here_mmddyyyy'].tolist()

enter_time_here_hhmm_pmam = df['_enter_time_here_hhmm_pmam'].astype(str).str.replace('\n', ' ').tolist()

select_timezone = df['_select_timezone'].tolist()

id = df['id'].tolist()

event_text = df['event_text'].tolist()

url = df['url'].tolist()

url_id= df['url_id'].tolist()

ids = []
nums = len(url_id)
for i in range(nums):
    ids.append(i+1)


dict = {'id': id, 'event_text': event_text, 'url': url, 'url_id': url_id, 'company': copy_the_company_name_from_the_text_gold, 'fiscal_year': select_fiscal_year_gold, 'fiscal_period': select_the_fiscal_period_check_as_many_as_it_applies_gold, 'event_type': please_select_the_event_type_gold, 'date': enter_date_here_mmddyyyy_gold, 'time': enter_time_here_hhmm_pmam_gold, 'timezone': select_timezone_gold}  

df = pd.DataFrame(dict)

df.to_csv('cleaned_appen.csv')