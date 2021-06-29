import pandas as pd
import os
from tqdm.auto import tqdm
import spacy

file_path = os.path.join('nasdaq_screener.csv')
df = pd.read_csv(file_path, sep=',', engine='python')
companies = list(df['Name'])


new_list = []
new_set = set()
for name in companies:

    first = name.split(',')
    first = first[0].split('(')
    first = first[0].split('Corp.')
    first = first[0].split('Inc.')

    # first = first[0].split('Inc')
    # first = first[0].split('Corp')
    # first = first[0].split('Corporation')
    # first = first[0].split('Limited')
    # first = first[0].split('Acquisition')

    first = first[0].split('Common')
    first = first[0].split('Holding')
    first = first[0].split('ETF')
    first = first[0].split('Ltd')
    first = first[0].split('Depositary')
    first = first[0].split('Preferred')
    first = first[0].split('Class')

    new_list.append(first[0])
    print(first[0])

print(len(new_list))
print(len(set(new_list)))


# dictionary of lists
dict = {'name': list(set(new_list))}

df = pd.DataFrame(dict)

# saving the dataframe
df.to_csv('company_names_nasdaq.csv', index=False)
