import pandas as pd

df1 = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "a", "b"],
                    "data1": [1, 2, 3, 4, 5, 6, 7]})
print(df1)

df2 = pd.DataFrame({"key": ['a', 'b', 'c'],
                    'data2': [10, 20, 30]})
print(df2)

joined = pd.merge(left=df1, right=df2, on="key", how='left')
print(joined)


# for the following, 
# do a left join, matching rows where both key1 *and* key2 match.
df1 = pd.DataFrame({"key1": ["b", "b", "a", "c", "a", "a", "d"],
                    'key2': ['a', 'a', 'b', 'b', 'c', 'c', 'd'],
                    "data1": [1, 2, 3, 4, 5, 6, 7]})

df2 = pd.DataFrame({"key1": ['a', 'b', 'c', 'e'],
                    'key2': ['a', 'a', 'b', 'd'],
                    'data2': [10, 20, 30, 40]})

merged = pd.merge(df1, df2, on=['key1', 'key2'], how='inner')
print(merged)

# now do an inner join 
# where the left table’s key1 matches right table’s key2
merged = pd.merge(df1, df2, left_on='key1', right_on='key2')
print(merged)
