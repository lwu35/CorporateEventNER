from sklearn.metrics import f1_score, accuracy_score
from sklearn import metrics
import pandas as pd


# gold_file = 'actual.csv'
# pred_file = 'predictions.csv'
gold_file = 'actual_eval.csv'
pred_file = 'predictions_eval.csv'


gold = pd.read_csv(gold_file, header=None)
pred = pd.read_csv(pred_file, header=None)

#print(gold.head())
print(metrics.classification_report(gold, pred))
#print(accuracy_score(gold, pred))


# def save_to_csv(url_list, name_list, date_list, time_list):
#     #"{Company}, {Fiscal Year}, {Fiscal Period}, {Event Type}, {Event Date}, {Time}, {Timezone}, {Language}, {Phone Number}, {Webcast URL}"
#     print('saving prediction')
#     event1 = []
#     event2 = []
#     event3 = []
#     event4 = []
#     event5 = []
#     blank = 'NONE'
#     empty = 'EMPTY'
#     for i in range(len(name_list)):
#         event1.append(
#             f'({name_list[i]}, {blank}, {blank}, {blank}, {date_list[i]}, {time_list[i]}, {blank}, {blank}, {blank}, {blank})')
#         event2.append(empty)
#         event3.append(empty)
#         event4.append(empty)
#         event5.append(empty)

#     table = {'Link': url_list, '1': event1, '2': event2,
#              '3': event3, '4': event4, '5': event5}
#     df = pd.DataFrame(table)
#     df.to_csv('predictions.csv', index=False)
