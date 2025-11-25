import pandas as pd


def series_range(series: pd.Series) -> float:
    """ custom aggregation - returns range of the series"""
    return series.max() - series.min()

df = pd.read_csv('./groupby/data.csv', index_col=None)

print(df.groupby('dept')['sales'].agg(series_range))


# here's an aggregation function that operates on whole groups
def custom_aggregation(frame: pd.DataFrame) -> float:
    """ get total sales for all products with rating > 60 """
    return frame.loc[frame['rating'] > 60, 'sales'].sum()

print(df.groupby('dept').apply(custom_aggregation))


df = pd.DataFrame({
        'date': ['2025-03-01','2025-03-01', '2025-03-02', '2025-03-02', '2025-03-03', '2025-03-03'],
        'customer': ['alice', 'bob', 'alice', 'charley', 'bob', 'charley'],
        'product': ['motherboard', 'ram', 'ram', 'ssd', 'ssd', 'ssd']
})

def is_ram_purchased(series: pd.Series) -> bool:
    return 'ram' in series.values

print(df.groupby('customer')['product'].agg(is_ram_purchased))
print(df.groupby('customer')['product'].agg(lambda s: 'ram' in s.values))

# another way:
def is_ram_purchased_df(df: pd.DataFrame) -> bool:
    return 'ram' in df['product'].values

print(df.groupby('customer').apply(is_ram_purchased_df))