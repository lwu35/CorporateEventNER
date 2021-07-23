import json
import pandas as pd


file_name = 'appen_1_2.json'
json_file = open(file_name, 'r', encoding="utf8")

"""
{"id":3077828077,"data":{"url_id":"1","url":"https://investors.astronics.com/news-events/ir-calendar"},"judgments_count":3,"state":"finalized","agreement":1.0,"missed_count":0,"gold_pool":null,"created_at":"2021-07-09T18:44:43+00:00","updated_at":"2021-07-20T03:28:56+00:00","job_id":1808791,"results":{"judgments":[{"id":6126074074,"created_at":"2021-07-19T13:20:28+00:00","started_at":"2021-07-19T13:18:16+00:00","acknowledged_at":null,"external_type":"cf_internal","golden":false,"missed":null,"rejected":null,"tainted":false,"country":"IND","region":"28","city":"Kolkata","unit_id":3077828077,"job_id":1808791,"worker_id":45232718,"trust":1,"worker_trust":0.953095858117445,"unit_state":"finalized","data":{"please_copy_entire_text_that_contains_schedule_information_related_to_a_single_corporate_event":["UBS Global Industrials and Transportation Virtual Conference\nJun 8, 2021","Q1 2021 Astronics Earnings Conference Call\nMay 6, 2021 • 11:00am EDT","Q4 2020 Astronics Earnings Conference Call\nFeb 23, 2021 • 11:00am EDT","Q4 2020 Astronics Earnings Conference Call\nFeb 23, 2021 • 11:00am EDT","Baird 2020 Global Industrial Conference\nNov 11, 2020"],"_clicks":["https://investors.astronics.com/news-events/ir-calendar"]},"unit_data":{"url_id":"1","url":"https://investors.astronics.com/news-events/ir-calendar"}},{"id":6126189742,"created_at":"2021-07-19T15:40:44+00:00","started_at":"2021-07-19T15:34:33+00:00","acknowledged_at":null,"external_type":"cf_internal","golden":false,"missed":null,"rejected":null,"tainted":false,"country":"IND","region":"28","city":"Kolkata","unit_id":3077828077,"job_id":1808791,"worker_id":46420152,"trust":1.0,"worker_trust":0.966107483993753,"unit_state":"finalized","data":{"please_copy_entire_text_that_contains_schedule_information_related_to_a_single_corporate_event":["UBS Global Industrials and Transportation Virtual Conference\nJun 8, 2021","2021 Astronics Corporation Annual Meeting of Shareholders\nMay 25, 2021 • 10:00am EDT","Q1 2021 Astronics Earnings Conference Call\nMay 6, 2021 • 11:00am EDT","Q4 2020 Astronics Earnings Conference Call\nFeb 23, 2021 • 11:00am EDT","Q3 2020 Astronics Earnings Conference Call\nOct 30, 2020 • 11:00am EDT"],"_clicks":["https://investors.astronics.com/news-events/ir-calendar"]},"unit_data":{"url_id":"1","url":"https://investors.astronics.com/news-events/ir-calendar"}},{"id":6126784264,"created_at":"2021-07-20T03:28:46+00:00","started_at":"2021-07-20T03:23:48+00:00","acknowledged_at":null,"external_type":"cf_internal","golden":false,"missed":null,"rejected":null,"tainted":false,"country":"IND","region":"28","city":"Kolkata","unit_id":3077828077,"job_id":1808791,"worker_id":45431031,"trust":1.0,"worker_trust":0.966729735499725,"unit_state":"finalized","data":{"please_copy_entire_text_that_contains_schedule_information_related_to_a_single_corporate_event":["UBS Global Industrials and Transportation Virtual Conference\nJun 8, 2021","2021 Astronics Corporation Annual Meeting of Shareholders\nMay 25, 2021 • 10:00am EDT\n\nOrlando, Florida","Q1 2021 Astronics Earnings Conference Call\nMay 6, 2021 • 11:00am EDT\n\n PDF HTMLEarnings Release\n AUDIOEarnings Webcast","Q4 2020 Astronics Earnings Conference Call\nFeb 23, 2021 • 11:00am EDT","Q3 2020 Astronics Earnings Conference Call\nOct 30, 2020 • 11:00am EDT\n\n PDF HTMLEarnings Release\n AUDIOEarnings Webcast"],"_clicks":["https://investors.astronics.com/news-events/ir-calendar"]},"unit_data":{"url_id":"1","url":"https://investors.astronics.com/news-events/ir-calendar"}}]}}

"""
count = 0
url_list = []
url_id_list = []
event_list = []
while True:
    # Get next line from file
    line = json_file.readline()
    count += 1
    # if line is empty
    # end of file is reached
    # if not line or count == 10:
    #     break
    if not line:
        break

    line_json = json.loads(line)

    # print(line_json.keys())

    # print('agreement:', line_json['agreement'], '\n')

    # print('data:', json.dumps(line_json['data'], indent=4))
    # print('results', json.dumps(line_json['results'], indent=4))
    # print('results', json.dumps(line_json['results']['judgments'], indent=4))
    # print(line_json['results']['judgments'][0]['data']
    #       ['please_copy_entire_text_that_contains_schedule_information_related_to_a_single_corporate_event'])

    if line_json['agreement'] == 1.0:
        data1 = line_json['results']['judgments'][0]['data']['please_copy_entire_text_that_contains_schedule_information_related_to_a_single_corporate_event']
        for i in data1:
            if i == "NO EVENTS FOUND":
                print(0)
                break
            event_text = i.replace('\n', ' ')
            url_list.append(line_json['data']['url'])
            url_id_list.append(line_json['data']['url_id'])
            event_list.append(event_text)

    elif line_json['agreement'] == 0.666666666666667:
        data1 = line_json['results']['judgments'][0]['data']['please_copy_entire_text_that_contains_schedule_information_related_to_a_single_corporate_event']
        data2 = line_json['results']['judgments'][1]['data']['please_copy_entire_text_that_contains_schedule_information_related_to_a_single_corporate_event']
        data3 = line_json['results']['judgments'][2]['data']['please_copy_entire_text_that_contains_schedule_information_related_to_a_single_corporate_event']
        if data1 == data2 or data1 == data3:
            for i in data1:
                if i == "NO EVENTS FOUND":
                    print(0)
                    break
                event_text = i.replace('\n', ' ')
                url_list.append(line_json['data']['url'])
                url_id_list.append(line_json['data']['url_id'])
                event_list.append(event_text)
        else:
            for i in data2:
                if i == "NO EVENTS FOUND":
                    print(0)
                    break
                event_text = i.replace('\n', ' ')
                url_list.append(line_json['data']['url'])
                url_id_list.append(line_json['data']['url_id'])
                event_list.append(event_text)

    else:
        data1 = line_json['results']['judgments'][0]['data']['please_copy_entire_text_that_contains_schedule_information_related_to_a_single_corporate_event']
        for i in data1:
            if i == "NO EVENTS FOUND":
                print(0)
                break
            event_text = i.replace('\n', ' ')
            url_list.append(line_json['data']['url'])
            url_id_list.append(line_json['data']['url_id'])
            event_list.append(event_text)

json_file.close()

table = {'url': url_list, 'url_id': url_id_list, 'event_text': event_list}
df = pd.DataFrame(table)
df.to_csv('appen_2.csv', index=True)


def agreement_count(file_name):
    json_file = open(file_name, 'r', encoding="utf8")
    count_dict = {}
    count_judgement = {}

    while True:
        line = json_file.readline()

        if not line:
            break

        line_json = json.loads(line)

        if line_json['agreement'] in count_dict:
            count_dict[line_json['agreement']] += 1
        else:
            count_dict[line_json['agreement']] = 1

        if line_json['judgments_count'] in count_judgement:
            count_judgement[line_json['judgments_count']] += 1
        else:
            count_judgement[line_json['judgments_count']] = 1

    print(count_dict)
    print(count_judgement)
    json_file.close()


# agreement_count(file_name)
