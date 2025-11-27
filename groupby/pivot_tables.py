import pandas as pd

df = pd.read_csv('./groupby/sales_data.csv', index_col=None)

pt = df.pivot_table(
    index=['dept', 'product'],
    columns='year',
    values='sales',
    aggfunc='sum'
)
print(pt)



#create a pivot table that shows:
#dept & product on the rows
#year and “> 85 rating” along the columns
#total sales and average rating as the values

df['>85 rating'] = df['rating'] > 85
pt = df.pivot_table(
    index=['dept', 'product'],
    columns=['year', '>85 rating'],
    values=['sales', 'rating'],
    aggfunc={'sales': 'sum','rating': 'mean'}
)
print(pt)

# get the total sales for houseware / rugs in 2016 with < 85 quality rating
print(pt.loc[('houseware', 'rug'), ('sales', 2016, False)])

# do the same thing, but use groupby this time
grouped = df.groupby(['dept', 'product', 'year', '>85 rating'])['sales'].agg('sum')
print(grouped[('houseware', 'rug', 2016, False)])