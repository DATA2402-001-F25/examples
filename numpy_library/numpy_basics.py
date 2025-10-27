import numpy as np
import time

my_list = [10] * 10_000

data1 = np.array(my_list)  # a 1-D array (vector)
data2 = np.array([[1, 2], [3, 4]])  # a 2-D array

# multiply the list by 2, the native python way
start = time.time()
for i in range(len(my_list)):
    my_list[i] *= 2
end = time.time()
print(end - start, 's elapsed')

# multiply the list by 2 the numpy way
start = time.time()
data1 *= 2
end = time.time()
print(end - start, 's elapsed')


# ndim and shape attributes
print(data1.ndim, data1.shape)
print(data2.ndim, data2.shape)

# some aggregation methods
print(data1.min())