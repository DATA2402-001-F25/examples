import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        'patient_id': [123, 521, 888, 123],
        'height': [1.8, 5.8, 1.6, 5.9],
        'weight': [140,  3000,  999,  140],
    }
)

# Some heights have been entered in m and some in ft. 
# Assume entries <2 are in m and convert them to ft (*3.3)
df.loc[df['height'] < 2, 'height'] = df.loc[df['height'] < 2, 'height'] * 3.3


# There are data entry errors in the weights, as some are outside 
# biological limits. Replace weights >300 with np.Nan
df.loc[df['weight'] > 300, 'weight'] = np.nan

print(df)



df = pd.DataFrame({
    'customer_name': ['eric', 'alice', 'bob'],
    'pizza_size': [8, 10, 12],
    'qty': [1, 1, 2],
})
# Compute order subtotal (add to dataframe as a new column)
# Calculate discount (customers named Eric get 10% discount)
# Calculate gst and total

df.loc[df['pizza_size'] == 8, 'price_per_pizza'] = 9
df.loc[df['pizza_size'] == 10, 'price_per_pizza'] = 12
df.loc[df['pizza_size'] == 12, 'price_per_pizza'] = 14

# another way:
df['price_per_pizza'] = df['pizza_size'].replace({8: 9, 10: 12, 12:14})
print(df)

# another way:
prices = {8: 9, 10: 12, 12:14}
for size, price in prices.items():
    df.loc[df['pizza_size'] == size, 'price_per_pizza'] = price

df['subtotal'] = df['price_per_pizza'] * df['qty']

# compute discount (10% for name == eric)
# df.loc[df['customer_name'] == 'eric', 'subtotal'] *= 0.9

# another way
df['discount'] = 0
df.loc[df['customer_name'] == 'eric', 'discount'] = df.loc[df['customer_name'] == 'eric', 'subtotal'] * 0.1

# another way
df['discount'] = df['subtotal'] * 0.1 * (df['customer_name'] == 'eric')

df['gst'] = (df['subtotal'] - df['discount']) * 0.05
df['total'] = df['subtotal'] - df['discount'] + df['gst']
print(df)
