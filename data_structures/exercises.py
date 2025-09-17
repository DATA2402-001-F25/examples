
months = ['jan', 'feb', 'mar', 'apr']
numbers = [1, 2, 3, 4]

def get_month_number(month_name: str) -> int:
    " do it using the lists above "
    for index in range(len(months)):
        if months[index] == month_name:
            return numbers[index]
    return -1

months_dictionary = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4}

def get_month_number_dict(month_name: str) -> int:
    try:
        return months_dictionary[month_name]
    except KeyError: # this handles the exception that occurs if the month_name isn't in the dict
        return -1

print(get_month_number_dict('dec'))




work_shifts = {
    'Alice': 'Weekdays',
    'Bob': 'Weekdays',
    'Charly': 'Weekends',
    'Denise': 'Weekdays'
}

# build 2 lists: people working weekends, and people working weekdays
weekends = []
weekdays = []

for name, shift in work_shifts.items():
    if shift == 'Weekends':
        weekends.append(name)
    else:
        weekdays.append(name)

print('weekends:', weekends)
print('weekdays:', weekdays)

# the fancy, but not necessary list-comprehension
weekends = [name for name in work_shifts.keys() if work_shifts[name] == 'Weekends']
print(weekends)