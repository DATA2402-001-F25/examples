import numpy as np

ar1 = np.array([1, 2, 3])
ar2 = np.array([3, 4, 5])

# multiply by scalar
print(ar1 * 2)  # gives [2, 4, 6]

# multiply equal-sized arrays
print(ar1 * ar2) # gives [3, 8, 15]


# comparing arrays of equal size
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[4, 3], [2, 1]])
print(arr1 > arr2)


# random walk exercise
arr = np.random.random(100) # 100 random numbers between 0 and 1
arr = arr * 2 - 1
arr = arr.cumsum()


# mean-square error between predictions and actuals
# (mean-square-error is the mean of the squares of the errors!)
predicted = np.array([2, 4, 1, 6, 8, 4])
actual = np.array([4, 4, 0, 3, 7, 6])

error = predicted - actual
sq_error = error * error  # or sq_error = error ** 2
mse = sq_error.mean()
print(mse)

# this would be a one-line version (multi-line probably clearer)
mse = ((predicted - actual) ** 2).mean()

# logical operations
arr = np.array([1, 2, 3, 4, 5, 6, 7])
bigger_than_4 = arr > 4
less_than_7 = arr < 7

print(bigger_than_4)
print(less_than_7)
print(bigger_than_4 & less_than_7)
