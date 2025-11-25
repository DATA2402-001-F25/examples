import pandas as pd

df = pd.read_csv('./groupby/data2.csv', index_col=None)


df['Date'] = pd.to_datetime(df['Date'])
df['month'] = df['Date'].dt.month

def compute_price_range(frame: pd.DataFrame) -> float:
    return frame['High'].max() - frame['Low'].min()

print(df.groupby('month').apply(compute_price_range))