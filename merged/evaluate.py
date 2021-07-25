import pandas as pd
import os
import sys
from tqdm.auto import tqdm
from fuzzywuzzy import fuzz

import datetime

from date_extractor import extract_dates
from dateparser.search import search_dates

from sklearn.metrics import accuracy_score, classification_report, f1_score


def main():

    if len(sys.argv) == 3:
        print(f'Comparing {sys.argv[1]} and {sys.argv[2]}')
        gold_file = sys.argv[1]
        pred_file = sys.argv[2]
    else:
        print('Comparing default files:')
        gold_file = 'job2_gold.csv'
        pred_file = 'bert_predictions.csv'

    file_path = os.path.join(gold_file)
    gold_df = pd.read_csv(file_path, sep=',', engine='python')

    file_path = os.path.join(pred_file)
    pred_df = pd.read_csv(file_path, sep=',', engine='python')

    checker(gold_df, pred_df)


def checker(gold_df, pred_df):

    gold_event_id = list(gold_df['id'])
    pred_event_id = list(pred_df['id'])

    gold_company = list(gold_df['company'])
    gold_fiscal_year = list(gold_df['fiscal_year'])
    gold_fiscal_period = list(gold_df['fiscal_period'])
    gold_event_type = list(gold_df['event_type'])
    gold_date = list(gold_df['date'])
    gold_time = list(gold_df['time'])
    gold_timezone = list(gold_df['timezone'])

    pred_company = list(pred_df['company'])
    pred_fiscal_year = list(pred_df['fiscal_year'])
    pred_fiscal_period = list(pred_df['fiscal_period'])
    pred_event_type = list(pred_df['event_type'])
    pred_date = list(pred_df['date'])
    pred_time = list(pred_df['time'])
    pred_timezone = list(pred_df['timezone'])

    count_company = []
    count_fiscal_year = []
    count_fiscal_period = []
    count_event_type = []
    count_date = []
    count_time = []
    count_timezone = []

    # fix issues like this: 'Apr\xa029,\xa02021'
    pred_date = date_space_checker(pred_date)

    gold_date, pred_date = date_converter(gold_date, pred_date)
    gold_time, pred_time = time_converter(gold_time, pred_time)

    for i in range(len(gold_event_id)):
        if gold_event_id[i] != pred_event_id[i]:
            print('EVENT ID MISMATCH')
            break

        # company comparison
        p_ratio = fuzz.partial_ratio(
            pred_company[i].lower(), gold_company[i].lower())
        ts_ratio = fuzz.token_set_ratio(pred_company[i], gold_company[i])

        if p_ratio >= 90 or ts_ratio >= 90:
            count_company.append(gold_company[i])
        else:
            count_company.append('WRONG')

        # fiscal year comparison
        if pred_fiscal_year[i] == gold_fiscal_year[i]:
            count_fiscal_year.append(gold_fiscal_year[i])
        else:
            count_fiscal_year.append('WRONG')

        # fiscal period comparison *INPROGRESS - NEEDS TO BE STANDARDIZED
        if pred_fiscal_period[i] == gold_fiscal_period[i]:
            count_fiscal_period.append(gold_fiscal_period[i])
        else:
            count_fiscal_period.append('WRONG')

        # event type comparison
        if pred_event_type[i] == gold_event_type[i]:
            count_event_type.append(gold_event_type[i])
        else:
            count_event_type.append('WRONG')

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

        # timezone comparison *INPROGRESS - NEEDS TO BE STANDARDIZED
        if pred_timezone[i] == gold_timezone[i]:
            count_timezone.append(gold_timezone[i])
        else:
            count_timezone.append('WRONG')

    # print(classification_report(gold_company, count_company))
    # print(classification_report(gold_date, count_date))
    # print(classification_report(gold_time, count_time))
    # print('Company Acc:', gold_company, count_company)
    # print('Date Acc:', gold_date, count_date)
    # print('Time Acc:', gold_time, count_time)

    print('Company Acc:', round(accuracy_score(gold_company, count_company), 3))
    print('Fiscal Year Acc:', round(accuracy_score(
        gold_fiscal_year, count_fiscal_year), 3))
    print('Fiscal Period Acc:', round(accuracy_score(
        gold_fiscal_period, count_fiscal_period), 3))
    print('Event Type Acc:', round(accuracy_score(
        gold_event_type, count_event_type), 3))
    print('Date Acc:', round(accuracy_score(gold_date, count_date), 3))
    # print('Date Acc:', f1_score(gold_date, count_date, average='micro'))
    print('Time Acc:', round(accuracy_score(gold_time, count_time), 3))
    print('Timezone Acc:', round(accuracy_score(gold_timezone, count_timezone), 3))

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


def date_space_checker(date_list):
    cleaned = []
    for date in date_list:
        cur = date.replace("\xa0", " ")
        cleaned.append(cur)
    return cleaned


if __name__ == '__main__':
    main()
