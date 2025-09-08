
line = '2024-10-03,AAPL,100.02,-2.3'

values = line.split(',') # gives ['2024-10-03', 'AAPL', '100.02', '-2.3']

# get the year/month/day
date_parts = values[0].split('-') # gives ['2024', '10', '03']

# get the closing price
open_price = float(values[2])
pct_change = float(values[3])
closing_price = open_price + pct_change/100 * open_price

print(closing_price)
