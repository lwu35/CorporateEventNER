import pandas as pd
import os
import sys
from tqdm.auto import tqdm
from fuzzywuzzy import fuzz

import datetime

from date_extractor import extract_dates
from dateparser.search import search_dates

from sklearn.metrics import accuracy_score, classification_report, f1_score, precision_score, recall_score, confusion_matrix
import configparser
import warnings
warnings.filterwarnings("ignore")


config = configparser.ConfigParser()
config.read('configg.ini')

log_file = open('eval_output.txt', 'w')
log_file_diff_company_name = open('diff_company.txt', 'w')
log_file_diff_f_y = open('diff_f_y.txt', 'w')
log_file_diff_f_p = open('diff_f_p.txt', 'w')
log_file_diff_e_t = open('diff_e_t.txt', 'w')
log_file_diff_d = open('diff_d.txt', 'w')
log_file_diff_t = open('diff_t.txt', 'w')
log_file_diff_t_z = open('diff_t_z.txt', 'w')

def main():

    if len(sys.argv) == 3:
        print(f'Comparing {sys.argv[1]} and {sys.argv[2]}')
        print(f'Comparing {sys.argv[1]} and {sys.argv[2]}',file = log_file)
        gold_file = sys.argv[1]
        pred_file = sys.argv[2]
    else:
        print('Comparing default files:')
        print('Comparing default files:',file = log_file)
        gold_file = config['pipeline']['INPUT_FILE']
        et_model = config['pipeline']['event_type_model']
        print('Using', et_model, 'for event type prediction')
        print('Using', et_model, 'for event type prediction',file = log_file)
        if et_model == 'bert':
            pred_file = config['pipeline']['bert_predictions']
        elif et_model == 'gpt':
            pred_file = config['pipeline']['GPT_OUTPUT']
        else:
            pred_file = config['pipeline']['REGEX_OUTPUT']

    file_path = os.path.join(gold_file)
    gold_df = pd.read_csv(file_path, sep=',', engine='python')

    file_path = os.path.join(pred_file)
    pred_df = pd.read_csv(file_path, sep=',', engine='python')

    single_fields(gold_df, pred_df)
    print('-------')
    full_fields(gold_df, pred_df)


def full_fields(gold_df, pred_df):

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

    count_all = []
    pred_all = []

    # fix issues like this: 'Apr\xa029,\xa02021'
    pred_date = date_space_checker(pred_date)

    # Normalize fields
    gold_fiscal_period, pred_fiscal_period = fiscal_period_converter(
        gold_fiscal_period, pred_fiscal_period)
    gold_date, pred_date = date_converter(gold_date, pred_date)
    gold_time, pred_time = time_converter(gold_time, pred_time)
    gold_timezone, pred_timezone = timezone_converter(
        gold_timezone, pred_timezone)

    for i in range(len(gold_event_id)):
        if gold_event_id[i] != pred_event_id[i]:
            print('EVENT ID MISMATCH')
            break

        cur_pred_all = []
        cur_count_all = []
        # company comparison
        p_ratio = fuzz.partial_ratio(
            pred_company[i].lower(), gold_company[i].lower())
        ts_ratio = fuzz.token_set_ratio(pred_company[i], gold_company[i])

        if p_ratio >= 90 or ts_ratio >= 90:
            cur_pred_all.append(gold_company[i])
        else:
            cur_pred_all.append('WRONG')
            print(i, pred_company[i], gold_company[i], file = log_file_diff_company_name, sep=',')

        cur_count_all.append(gold_company[i])

        # fiscal year comparison
        if pred_fiscal_year[i] == gold_fiscal_year[i]:
            cur_pred_all.append(gold_fiscal_year[i])
        else:
            cur_pred_all.append(pred_fiscal_year[i])
            print(i, pred_fiscal_year[i], gold_fiscal_year[i], file = log_file_diff_f_y, sep=',')
        cur_count_all.append(gold_fiscal_year[i])

        # fiscal period comparison
        if pred_fiscal_period[i] == gold_fiscal_period[i]:
            cur_pred_all.append(gold_fiscal_period[i])
        else:
            cur_pred_all.append(pred_fiscal_period[i])
            print(i, pred_fiscal_period[i], gold_fiscal_period[i], file = log_file_diff_f_p, sep=',')
        cur_count_all.append(gold_fiscal_period[i])

        # event type comparison
        if pred_event_type[i] == gold_event_type[i]:
            cur_pred_all.append(gold_event_type[i])
        else:
            cur_pred_all.append(pred_event_type[i])
            print(i, pred_event_type[i], gold_event_type[i], file = log_file_diff_e_t, sep=',')
        cur_count_all.append(gold_event_type[i])

        # date comparison
        if pred_date[i] == gold_date[i]:
            cur_pred_all.append(gold_date[i])
        else:
            cur_pred_all.append(pred_date[i])
            print(i, pred_date[i], gold_date[i], file = log_file_diff_d, sep=',')
        cur_count_all.append(gold_date[i])

        # time comparison
        if pred_time[i] == gold_time[i]:
            cur_pred_all.append(gold_time[i])
        else:
            cur_pred_all.append(pred_time[i])
            print(i, pred_time[i], gold_time[i], file = log_file_diff_t, sep=',')
        cur_count_all.append(gold_time[i])

        # timezone comparison
        if pred_timezone[i] == gold_timezone[i]:
            cur_pred_all.append(gold_timezone[i])
        else:
            cur_pred_all.append(pred_timezone[i])
            print(i, pred_timezone[i], gold_timezone[i], file = log_file_diff_t_z, sep=',')
        cur_count_all.append(gold_timezone[i])

        count_all.append(str(tuple(cur_count_all)))
        pred_all.append(str(tuple(cur_pred_all)))

    print_score('Event tuples:', count_all, pred_all)

    return 0


def single_fields(gold_df, pred_df):

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

    gold_count_company = []
    gold_count_fiscal_year = []
    gold_count_fiscal_period = []
    gold_count_event_type = []
    gold_count_date = []
    gold_count_time = []
    gold_count_timezone = []

    # fix issues like this: 'Apr\xa029,\xa02021'
    pred_date = date_space_checker(pred_date)

    # Normalize fields
    gold_fiscal_period, pred_fiscal_period = fiscal_period_converter(
        gold_fiscal_period, pred_fiscal_period)
    gold_date, pred_date = date_converter(gold_date, pred_date)
    gold_time, pred_time = time_converter(gold_time, pred_time)
    gold_timezone, pred_timezone = timezone_converter(
        gold_timezone, pred_timezone)

    for i in range(len(gold_event_id)):
        if gold_event_id[i] != pred_event_id[i]:
            print('EVENT ID MISMATCH')
            print('EVENT ID MISMATCH', file = log_file)
            break

        # company comparison
        if gold_company[i] != 'NONE' or pred_company[i] != 'NONE':
            p_ratio = fuzz.partial_ratio(
                pred_company[i].lower(), gold_company[i].lower())
            ts_ratio = fuzz.token_set_ratio(pred_company[i], gold_company[i])

            if p_ratio >= 90 or ts_ratio >= 90:
                count_company.append(gold_company[i])
            else:
                count_company.append('WRONG')
            gold_count_company.append(gold_company[i])

        # fiscal year comparison
        if gold_fiscal_year[i] != 'NONE' or pred_fiscal_year[i] != 'NONE':
            if pred_fiscal_year[i] == gold_fiscal_year[i]:
                count_fiscal_year.append(gold_fiscal_year[i])
            else:
                count_fiscal_year.append(pred_fiscal_year[i])
            gold_count_fiscal_year.append(gold_fiscal_year[i])

        # fiscal period comparison
        if gold_fiscal_period[i] != 'NONE' or pred_fiscal_period[i] != 'NONE':
            if pred_fiscal_period[i] == gold_fiscal_period[i]:
                count_fiscal_period.append(gold_fiscal_period[i])
            else:
                count_fiscal_period.append(pred_fiscal_period[i])
            gold_count_fiscal_period.append(gold_fiscal_period[i])

        # event type comparison
        if gold_event_type[i] != 'NONE' or pred_event_type[i] != 'NONE':
            if pred_event_type[i] == gold_event_type[i]:
                count_event_type.append(gold_event_type[i])
            else:
                count_event_type.append(pred_event_type[i])
            gold_count_event_type.append(gold_event_type[i])

        # date comparison
        if gold_date[i] != 'NONE' or pred_date[i] != 'NONE':
            if pred_date[i] == gold_date[i]:
                count_date.append(gold_date[i])
            else:
                count_date.append(pred_date[i])
            gold_count_date.append(gold_date[i])

        # time comparison
        if gold_time[i] != 'NONE' or pred_time[i] != 'NONE':
            if pred_time[i] == gold_time[i]:
                count_time.append(gold_time[i])
            else:
                count_time.append(pred_time[i])
            gold_count_time.append(gold_time[i])

        # timezone comparison
        if gold_timezone[i] != 'NONE' or pred_timezone[i] != 'NONE':
            if pred_timezone[i] == gold_timezone[i]:
                count_timezone.append(gold_timezone[i])
            else:
                count_timezone.append(pred_timezone[i])
            gold_count_timezone.append(gold_timezone[i])

    print_score('Company', gold_count_company, count_company)
    print_score('Fiscal Year', gold_count_fiscal_year, count_fiscal_year)
    print_score('Fiscal Period', gold_count_fiscal_period, count_fiscal_period)
    print_score('Event Type', gold_count_event_type, count_event_type)
    print_score('Date', gold_count_date, count_date)
    print_score('Time', gold_count_time, count_time)
    print_score('Timezone', gold_count_timezone, count_timezone)

    # print(confusion_matrix(gold_count_date, count_date))
    # print(classification_report(gold_count_fiscal_period, count_fiscal_period))

    return 0


def print_score(field, gold_count, count):
    if field == 'Time' or field == 'Date':
        print(f'{field} \t\t({len(gold_count)} examples) \t\tAcc::', round(accuracy_score(
            gold_count, count), 3), f'\tF1:', round(f1_score(
                gold_count, count, average='macro'), 3))
        print(f'{field} \t\t({len(gold_count)} examples) \t\tAcc::', round(accuracy_score(
            gold_count, count), 3), f'\tF1:', round(f1_score(
                gold_count, count, average='macro'), 3),file = log_file)
    else:
        print(f'{field} \t({len(gold_count)} examples) \t\tAcc::', round(accuracy_score(
            gold_count, count), 3), f'\tF1:', round(f1_score(
                gold_count, count, average='macro'), 3))
        print(f'{field} \t({len(gold_count)} examples) \t\tAcc::', round(accuracy_score(
            gold_count, count), 3), f'\tF1:', round(f1_score(
                gold_count, count, average='macro'), 3),file = log_file)


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


def fiscal_period_converter(gold_fiscal_period, pred_fiscal_period):
    converted_gold = []
    converted_pred = []

    fp_mapping = {
        'q1': 'Q1', '1q': 'Q1', 'quarter 1': 'Q1', 'first quarter': 'Q1',
        'q2': 'Q2', '2q': 'Q2', 'quarter 2': 'Q2', 'second quarter': 'Q2',
        'q3': 'Q3', '3q': 'Q3', 'quarter 3': 'Q3', 'third quarter': 'Q3',
        'q4': 'Q4', '4q': 'Q4', 'quarter 4': 'Q4', 'fourth quarter': 'Q4',
        'full year': 'Y', 'annual': 'Y', 'full': 'Y', 'yearly': 'Y', 'y': 'Y',
        'first half': 'S1', 'semi annual 1': 'S1', 'semi-annual 1': 'S1', 'first semi-annual': 'S1', 'first semi annual': 'S1',
        'second half': 'S2', 'semi annual 2': 'S2', 'semi-annual 2': 'S2', 'second semi-annual': 'S2', 'second semi annual': 'S2',
        'none': 'NONE'
    }
    for i in range(len(gold_fiscal_period)):
        cur_gold_fiscal_period = gold_fiscal_period[i].lower().strip()
        cur_pred_fiscal_period = pred_fiscal_period[i].lower().strip()

        if cur_gold_fiscal_period in fp_mapping:
            cur_gold_fiscal_period = fp_mapping[cur_gold_fiscal_period]
        if cur_pred_fiscal_period in fp_mapping:
            cur_pred_fiscal_period = fp_mapping[cur_pred_fiscal_period]

        converted_gold.append(cur_gold_fiscal_period)
        converted_pred.append(cur_pred_fiscal_period)

    return converted_gold, converted_pred


def timezone_converter(gold_timezone, pred_timezone):
    converted_gold = []
    converted_pred = []

    timezone_mapping = {
        'PDT': 'PST', 'PT': 'PST',
        'MDT': 'MST', 'MT': 'MST',
        'CDT': 'CST', 'CT': 'CST',
        'EDT': 'EST', 'ET': 'EST',
        'none': 'NONE'
    }
    for i in range(len(gold_timezone)):
        cur_gold_timezone = gold_timezone[i].upper().strip()
        cur_pred_timezone = pred_timezone[i].upper().strip()

        if cur_gold_timezone in timezone_mapping:
            cur_gold_timezone = timezone_mapping[cur_gold_timezone]
        if cur_pred_timezone in timezone_mapping:
            cur_pred_timezone = timezone_mapping[cur_pred_timezone]

        converted_gold.append(cur_gold_timezone)
        converted_pred.append(cur_pred_timezone)

    return converted_gold, converted_pred


def date_space_checker(date_list):
    cleaned = []
    for date in date_list:
        cur = date.replace("\xa0", " ")
        cleaned.append(cur)
    return cleaned


if __name__ == '__main__':
    main()
