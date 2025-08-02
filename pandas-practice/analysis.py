# %%
import pandas as pd
df = pd.read_csv('hotel-booking-data.txt', delimiter = '\t')
df.head()
# %%
df.dropna()
# %%
df.describe()
# %%
