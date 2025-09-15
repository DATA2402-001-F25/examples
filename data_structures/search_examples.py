
# how long does it take to run in the worst case
my_list = ['a'] * 20_000_000 + ['hello world']

import time
start_time = time.time()
index = search(my_list, "hello world")
end_time = time.time()

print(f'index={index:,}, {(end_time - start_time)*1000:.2f} milliseconds elapsed')

