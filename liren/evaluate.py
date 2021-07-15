import pandas as pd
import os
import sys
from tqdm.auto import tqdm
from fuzzywuzzy import fuzz

import datetime

from date_extractor import extract_dates
from dateparser.search import search_dates

from sklearn.metrics import accuracy_score, classification_report, f1_score


NUM_EX = 50


def main():

    if len(sys.argv) == 3:
        print(f'Comparing {sys.argv[1]} and {sys.argv[2]}')
        gold_file = sys.argv[1]
        pred_file = sys.argv[2]
    else:
        print('Comparing default files:')
        gold_file = '160_links_cleaned.csv'
        pred_file = 'predictions.csv'

    file_path = os.path.join(gold_file)
    gold_df = pd.read_csv(file_path, sep=',', engine='python')

    file_path = os.path.join(pred_file)
    pred_df = pd.read_csv(file_path, sep=',', engine='python')

    print(f'Testing: {NUM_EX} examples')
    checker(gold_df, pred_df, NUM_EX, '1')


def checker(gold_df, pred_df, num_ex, event_col):
    gold_link = list(gold_df['Link'][:num_ex])
    pred_link = list(pred_df['Link'][:num_ex])

    gold_tuple = list(gold_df[event_col][:num_ex])
    pred_tuple = list(pred_df[event_col][:num_ex])

    gold_company = []
    gold_fiscal_year = []
    gold_fiscal_period = []
    gold_event_type = []
    gold_date = []
    gold_time = []

    for i, page in enumerate(gold_tuple):
        # print(page)
        # print(i)
        if page != 'EMPTY':
            page = page[1:-1]
            event_info = page.split(',')

            gold_company.append(event_info[0].strip())
            gold_fiscal_year.append(event_info[1].strip())
            gold_fiscal_period.append(event_info[2].strip())
            gold_event_type.append(event_info[3].strip())
            gold_date.append(event_info[4].strip())

            gold_time.append(event_info[5].strip())
            # gold_timezone.append(event_info[6].strip())
            # gold_language.append(event_info[7].strip())
            # gold_phone_num.append(event_info[8].strip())
            # gold_webcast.append(event_info[9].strip())

        else:
            gold_company.append('NONE')
            gold_fiscal_year.append('NONE')
            gold_fiscal_period.append('NONE')
            gold_event_type.append('NONE')
            gold_date.append('NONE')

            gold_time.append('NONE')
            # gold_timezone.append('NONE')
            # gold_language.append('NONE')
            # gold_phone_num.append('NONE')
            # gold_webcast.append('NONE')

    pred_company = []
    pred_date = []
    pred_time = []
    pred_fiscal_year = []
    pred_fiscal_period = []
    pred_event_type = []

    for page in pred_tuple:
        # print(page)
        page = page[1:-1]
        event_info = page.split(',')

        pred_company.append(event_info[0].strip())
        pred_fiscal_year.append(event_info[1].strip())
        pred_fiscal_period.append(event_info[2].strip())
        pred_event_type.append(event_info[3].strip())
        pred_date.append(event_info[4].strip())

        pred_time.append(event_info[5].strip())
        # pred_timezone.append(event_info[6].strip())
        # pred_language.append(event_info[7].strip())
        # pred_phone_num.append(event_info[8].strip())
        # pred_webcast.append(event_info[9].strip())

    count_company = []
    count_fiscal_year = []
    count_fiscal_period = []
    count_event_type = []
    count_date = []
    count_time = []

    gold_date, pred_date = date_converter(gold_date, pred_date)
    gold_time, pred_time = time_converter(gold_time, pred_time)

    for i in range(num_ex):
        if gold_link[i] != pred_link[i]:
            print('URL MISMATCH')
            break

        # company comparison
        p_ratio = fuzz.partial_ratio(
            pred_company[i].lower(), gold_company[i].lower())
        ts_ratio = fuzz.token_set_ratio(pred_company[i], gold_company[i])
        if p_ratio >= .9 or ts_ratio >= .9:
            count_company.append(gold_company[i])
        else:
            count_company.append('WRONG')

        # date comparison
        if pred_date[i] == gold_date[i]:
            count_date.append(gold_date[i])
        else:
            count_date.append(datetime.date(
                1000, 10, 10).strftime("%b %d, %Y"))

        # time comparison
        if pred_time[i] == gold_time[i]:
            count_time.append(gold_time[i])
        else:
            count_time.append(datetime.time(0, 0, 30).strftime("%H:%M:%S"))

    # print(classification_report(gold_company, count_company))
    # print(classification_report(gold_date, count_date))
    # print(classification_report(gold_time, count_time))
    # print('Company Acc:', gold_company, count_company)
    # print('Date Acc:', gold_date, count_date)
    # print('Time Acc:', gold_time, count_time)

    print('Company Acc:', accuracy_score(gold_company, count_company))
    print('Date Acc:', accuracy_score(gold_date, count_date))
    # print('Date Acc:', f1_score(gold_date, count_date, average='micro'))
    print('Time Acc:', accuracy_score(gold_time, count_time))

    return 0


def date_converter(gold_dates, pred_dates):
    converted_gold = []
    converted_pred = []
    for i in range(len(gold_dates)):
        cur_pred_date = datetime.date(1000, 2, 2)
        cur_gold_date = datetime.date(1000, 1, 1)
        if len(extract_dates(pred_dates[i])) == 1:
            cur_pred_date = extract_dates(pred_dates[i])[0].date()
        if len(extract_dates(gold_dates[i])) == 1:
            cur_gold_date = extract_dates(gold_dates[i])[0].date()
        converted_gold.append(cur_gold_date.strftime("%b %d, %Y"))
        converted_pred.append(cur_pred_date.strftime("%b %d, %Y"))

    return converted_gold, converted_pred


def time_converter(gold_times, pred_times):
    converted_gold = []
    converted_pred = []
    for i in range(len(gold_times)):
        gold_times[i] = gold_times[i].upper().replace('AM', 'A.M')
        gold_times[i] = gold_times[i].upper().replace('PM', 'P.M')
        pred_times[i] = pred_times[i].upper().replace('AM', 'A.M')
        pred_times[i] = pred_times[i].upper().replace('PM', 'P.M')

        cur_pred_time = datetime.time(1, 1, 30)
        cur_gold_time = datetime.time(2, 2, 30)

        if search_dates(gold_times[i]) != None:
            cur_gold_time = search_dates(gold_times[i])[0][1].time()
        if search_dates(pred_times[i]) != None:
            cur_pred_time = search_dates(pred_times[i])[0][1].time()

        converted_gold.append(cur_gold_time.strftime("%H:%M:%S"))
        converted_pred.append(cur_pred_time.strftime("%H:%M:%S"))

    return converted_gold, converted_pred


if __name__ == '__main__':
    main()
