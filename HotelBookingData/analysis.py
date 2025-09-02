# %%
import pandas as pd
import numpy as np

df = pd.read_csv('/home/ant/Documents/projects/pandas-practice/HotelBookingData/hotel-booking-data.txt', delimiter = '\t')
df.head()
# %%
df.dropna()
# %%
df.describe()
# %%
df.value_counts('Company')

# %%
df2 = df.value_counts('Company')
df2.plot()
# %%
mask = df['Room number'].isna()

df['Booking Method'] = np.where(mask, df['Date'], np.nan)
df
# %%
df['Booking Method'].fillna(method = 'bfill', inplace=True)
df
# %%
df.dropna(inplace=True)
df
# %%
df2 = df.value_counts('Booking Method')
df2.plot()
# %%
df.tail()
# %%
df.head()
df
# %%
