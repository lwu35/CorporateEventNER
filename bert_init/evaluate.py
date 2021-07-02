from sklearn.metrics import f1_score, accuracy_score
from sklearn import metrics
import pandas as pd


gold_file = 'actual.csv'
pred_file = 'predictions.csv'


gold = pd.read_csv(gold_file, header=None)
pred = pd.read_csv(pred_file, header=None)

#print(gold.head())
print(metrics.classification_report(gold, pred))
#print(accuracy_score(gold, pred))