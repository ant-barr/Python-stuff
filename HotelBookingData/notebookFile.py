import pandas as pd
import numpy as np

df = pd.read_csv('pandas-practice\\hotel-booking-data.txt', delimiter = '\t')
print(df.head())

print(' ')

print(df.describe())

print(' ')

print(df['Company'].value_counts())

print(' ')

print(df.dropna())