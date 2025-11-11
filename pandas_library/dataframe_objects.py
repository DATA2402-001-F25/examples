import pandas as pd

data = {
    "Day": ["Monday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Product": ["Apples", "Bananas", "Apples", "Oranges", "Apples", "Bananas", "Oranges", "Bananas"],
    "Units Sold": [10, 15, 8, 12, 14, 20, 10, 18],
    "Price per Unit ($)": [1.5, 0.8, 1.5, 1.2, 1.5, 0.8, 1.2, 0.8],
}
df = pd.DataFrame(data)

# Compute a new series showing total sales for each row (units * price)
total_sales = df['Units Sold'] * df['Price per Unit ($)']
print(total_sales)

# Add this series to the DataFrame as a new column named “total sales”
df['total sales'] = total_sales
print(df)

# (or do it all in one step)
df['total sales'] = df['Units Sold'] * df['Price per Unit ($)']

# Filter the dataframe to only rows with >10 units sold
df = df.loc[df['Units Sold'] > 10, :]
print(df)
