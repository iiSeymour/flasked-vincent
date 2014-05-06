import random
import pandas as pd

"""
Some data to plot, pull from:

http://vincent.readthedocs.org/en/latest/quickstart.html#quick-data

Copyright 2013, Rob Story, Dan Miller, et. al..
"""

#Iterable
list_data = [10, 20, 30, 20, 15, 30, 45]

#Dicts of iterables
cat_1 = ['y1', 'y2', 'y3', 'y4']
index_1 = range(0, 21, 1)
multi_iter1 = {'index': index_1}
for cat in cat_1:
    multi_iter1[cat] = [random.randint(10, 100) for x in index_1]

cat_2 = ['y' + str(x) for x in range(0, 10, 1)]
index_2 = range(1, 21, 1)
multi_iter2 = {'index': index_2}
for cat in cat_2:
    multi_iter2[cat] = [random.randint(10, 100) for x in index_2]

farm_1 = {'apples': 10, 'berries': 32, 'squash': 21, 'melons': 13, 'corn': 18}
farm_2 = {'apples': 15, 'berries': 43, 'squash': 17, 'melons': 10, 'corn': 22}
farm_3 = {'apples': 6, 'berries': 24, 'squash': 22, 'melons': 16, 'corn': 30}
farm_4 = {'apples': 12, 'berries': 30, 'squash': 15, 'melons': 9, 'corn': 15}

farm_data = [farm_1, farm_2, farm_3, farm_4]
farm_index = ['Farm 1', 'Farm 2', 'Farm 3', 'Farm 4']
df_farm = pd.DataFrame(farm_data, index=farm_index)

#As DataFrames
index_3 = multi_iter2.pop('index')
df_1 = pd.DataFrame(multi_iter2, index=index_3)
df_1 = df_1.reindex(columns=sorted(df_1.columns))

cat_4 = ['Metric_' + str(x) for x in range(0, 10, 1)]
index_4 = ['Data 1', 'Data 2', 'Data 3', 'Data 4']
data_3 = {}
for cat in cat_4:
    data_3[cat] = [random.randint(10, 100) for x in index_4]
df_2 = pd.DataFrame(data_3, index=index_4)

import pandas.io.data as web
all_data = {}
for ticker in ['AAPL', 'IBM', 'YHOO', 'MSFT']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2012', '1/1/2014')
price = pd.DataFrame({tic: data['Adj Close'] for tic, data in all_data.iteritems()})
