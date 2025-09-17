from tuple_examples import search

# how long does it take to run in the worst case
my_list = ['a'] * 20_000_000 + ['hello world']

import time
start_time = time.time()
index = search(my_list, "hello world")
end_time = time.time()

print(f'index={index:,}, {(end_time - start_time)*1000:.2f} milliseconds elapsed')



# try it with a set
my_set = set()
for i in range(10_000_000):
    my_set.add(i)

start_time = time.time()
print(9_999_999 in my_set)
end_time = time.time()
print(f'{(end_time - start_time)*1000:.2f} milliseconds elapsed with a set')


