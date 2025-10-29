import numpy as np


my_list = ['a', 'b', 'c']
print(my_list[0]) # the first thing in the list
print(my_list[-1]) # the last thing in the list
print(my_list[1:]) # a "slice" that starts at index 1 and goes to the end

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr[2:5])
arr[2:5] = 10
print(arr)
arr[2:5] = np.array([10, 20 ,30])
print(arr)


# a slice of a list is a new list
my_slice = my_list[1:]
print(my_list, my_slice)
my_slice[0] = 'z'
print(my_list, my_slice)

# a slice of an ndarray is a "view" into the original array
arr_slice = arr[2:5]
print(arr, arr_slice)
arr_slice[0] = 100
print(arr, arr_slice)

# 2D slicing (python lists)
twoD_list = [[1, 2], [3, 4]]
twoD_list[0][0] # gets the #1 from the top left corner

# 2D slicing (numpy arrays)
twoD_arr = np.array([[1, 2], [3, 4]])
twoD_arr[0, 0] # gets the #1 from the top left corner of the array


# boolean indexing
arr = np.array([1, 2, 3, 4, 5, 6])
bigger_than_4 = arr > 4  # this is a boolean array
print(arr[bigger_than_4])  # prints([5, 6]), where bigger_than_4 was true


scores = np.array([
    ['alice', 5],
    ['bob', 3],
    ['cindy', 4],
    ['bob', 10]
])
print(scores)
bob_rows = scores[:, 0] == 'bob'
bob_score = scores[bob_rows, 1]
print(bob_rows)
print(bob_score)
