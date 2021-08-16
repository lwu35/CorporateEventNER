import re
from date_extractor import extract_dates
from dateparser.search import search_dates


def normalize_date(date_str):
    if date_str == 'NONE' or len(date_str) == 0:
        return 'NONE'
    else:
        if len(extract_dates(date_str)) >= 1:
            cur_date = extract_dates(date_str)[0].date()
            return cur_date.strftime("%b %d, %Y")
    return 'NONE'


def normalize_time(time_str):

    if time_str == 'NONE':
        return 'NONE'
    else:
        time_str = time_str.replace(" ", "")
        time_str = time_str.upper().replace('AM', 'A.M')
        time_str = time_str.replace('PM', 'P.M')
        time_str = time_str.replace('AM', 'A.M')
        time_str = time_str.replace('PM', 'P.M')

        if search_dates(time_str) != None:
            cur_time = search_dates(time_str)[0][1].time()
            return cur_time.strftime("%I:%M %p")

    return 'NONE'


def normalize_fiscal_period(fp_str):

    fp_mapping = {
        'q1': 'Q1', '1q': 'Q1', 'quarter 1': 'Q1', 'first quarter': 'Q1', '1st quarter': 'Q1',
        'q2': 'Q2', '2q': 'Q2', 'quarter 2': 'Q2', 'second quarter': 'Q2', '2nd quarter': 'Q2',
        'q3': 'Q3', '3q': 'Q3', 'quarter 3': 'Q3', 'third quarter': 'Q3', '3rd quarter': 'Q3',
        'q4': 'Q4', '4q': 'Q4', 'quarter 4': 'Q4', 'fourth quarter': 'Q4', '4th quarter': 'Q4',
        'full year': 'Y', 'annual': 'Y', 'full': 'Y', 'yearly': 'Y', 'y': 'Y',
        'first half': 'S1', 'semi annual 1': 'S1', 'semi-annual 1': 'S1', 'first semi-annual': 'S1', 'first semi annual': 'S1',
        'second half': 'S2', 'semi annual 2': 'S2', 'semi-annual 2': 'S2', 'second semi-annual': 'S2', 'second semi annual': 'S2',
        'none': 'NONE'
    }

    fp_str = fp_str.lower().strip()

    if fp_str in fp_mapping:
        cur_fp = fp_mapping[fp_str]
        return cur_fp

    return 'NONE'


def timezone_converter(timezone_str):

    only_alpha = re.compile('[^a-zA-Z\s]')

    timezone_str = only_alpha.sub('', timezone_str).upper().strip()

    return timezone_str
