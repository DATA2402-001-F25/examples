from pandas import Series

temperature = Series(
    [22.5, 24, 19.8, 21, 23.3, 25.1, 20.7],
    index=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    name='temperatures'
)
print(temperature)

# Find the difference between the max and min temperatures
print(temperature.max() - temperature.min())


# Get the names of the days with temperatures > 22
temp = temperature > 22
print(temperature[temp].index)
#or
print(temperature[temperature > 22].index)

# Create a new series of temperatures in °F    (F=C×9/5​+32)
temperatures_f = temperature * 9/5 + 32
print(temperatures_f)