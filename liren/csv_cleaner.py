import pandas as pd
import os
import numpy as np


file_path = os.path.join('160_links.csv')
df = pd.read_csv(file_path, sep=',', engine='python')

df.drop(columns=['Type', 'HTML Header'], inplace=True)
df.replace(np.nan, 'EMPTY', regex=True, inplace=True)

df.to_csv('160_links_cleaned.csv', index=False)
