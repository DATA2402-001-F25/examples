import pandas as pd

df1 = pd.DataFrame({"key": ["a", "a", "b", "c", "c", "d", "d"],
                    "data": [1, 2, 3, 4, 5, 6, 7]})

df2 = pd.DataFrame({"key": ['a', 'b', 'c', 'e'],
                    'data': [10, 20, 30, 40]})

joined = pd.merge(df1, df2, on='key', suffixes=('_left', '_right'))
print(joined)