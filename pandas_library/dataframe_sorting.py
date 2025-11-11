import pandas as pd

df = pd.DataFrame({
    "Day": ["Monday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Product": ["Apples", "Bananas", "Apples", "Oranges", "Apples", "Bananas", "Oranges", "Bananas"],
    "Units Sold": [10, 15, 8, 12, 14, 20, 10, 18],
    "Price per Unit ($)": [1.5, 0.8, 1.5, 1.2, 1.5, 0.8, 1.2, 0.8],
})

# Get the table row with the minimum “total sales”. Use “Units Sold” to break ties
df['total_sales'] = df['Units Sold'] * df['Price per Unit ($)']
df = df.sort_values(['total_sales', 'Units Sold'])
print(df)
print(df.iloc[0, :]) # gets the first row, using .iloc (numpy-style indexint)