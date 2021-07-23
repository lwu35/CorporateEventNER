import pandas as pd
url_file = 'job2_init.csv'
pred_file = 'predictions_eval.csv'

urls_pd = pd.read_csv(url_file)
#print(urls_pd.head())
url_list = urls_pd["url"].tolist()

pred = pd.read_csv(pred_file, header=None)

event_type = pred.values.tolist()
event_type = [v[0] for v in event_type]
print(event_type)
def save_to_csv(url_list, event_type):
    #"{Company}, {Fiscal Year}, {Fiscal Period}, {Event Type}, {Event Date}, {Time}, {Timezone}, {Language}, {Phone Number}, {Webcast URL}"
    print('saving prediction')
    event1 = []
    event2 = []
    event3 = []
    event4 = []
    event5 = []
    blank = 'NONE'
    empty = 'EMPTY'
    for i in range(len(event_type)):
        event1.append(
            f'({blank}, {blank}, {blank}, {event_type[i]}, {blank}, {blank}, {blank}, {blank}, {blank}, {blank})')
        event2.append(empty)
        event3.append(empty)
        event4.append(empty)
        event5.append(empty)

    table = {'Link': url_list, '1': event1, '2': event2,
             '3': event3, '4': event4, '5': event5}
    df = pd.DataFrame(table)
    df.to_csv('predictions_event_type.csv', index=False)

save_to_csv(url_list, event_type)