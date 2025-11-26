import pandas as pd


df = pd.read_csv('./groupby/sales_data.csv', index_col=None)
print(df)

# get total sales for each dept
total_sales = df.groupby('dept')['sales'].sum()
print(total_sales)
# now get the total sales for houseware
print(total_sales['houseware'])

# to group by more than one column
total_sales = df.groupby(['dept', 'year'])['sales'].sum()
print(total_sales)
# now indices are dept-year tuples
print(total_sales[('houseware', 2015)])

# alternate syntax for aggregation
print(df.groupby('dept')['sales'].agg('sum'))
# or do multiple aggregations
print(df.groupby('dept')['sales'].agg(['sum', 'mean']))

# or do multiple aggregations on multiple columns
grouped = df.groupby('dept')[['sales', 'rating']].agg(['sum', 'mean'])
print(grouped)
print(grouped[('sales', 'sum')]) # access compound-column name

# do different aggregations on different columns
print(df.groupby(['dept', 'year'])[['sales', 'rating']].agg({
        'sales': 'sum',
        'rating': ['min', 'max']
    }
))