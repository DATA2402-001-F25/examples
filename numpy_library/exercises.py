import numpy as np

arr = np.array([1, -2, 3, 0, -4, 2])
is_negative = arr < 0
arr[is_negative] = 0
print(arr)


scores = np.array([
    ['alice', 5],
    ['bob', 3],
    ['cindy', 4],
    ['david', 1],
    ['edith', 2]
])
print(scores[[1, 2, 4], 1]) # this is one way, hard-coding the indices

# but this would work even if the rows were in different order:
is_alice = scores[:, 0] == 'alice'
is_david = scores[:, 0] == 'david'
alice_or_david = is_alice | is_david
print(scores[~alice_or_david, :])


# Taxicab distance exercise
coords = np.random.random((100, 2)) # 100 random (x,y) coordinates
current = np.array([0.5, 0.5])

# substract coords from current (broadcasts - gives a 100x2 result)
differences = coords - current

# absolute value
differences = np.abs(differences)

# add dx to dy
taxicab = differences[:, 0] + differences[:, 1]
# or
taxicab = differences.sum(axis=1)
print(taxicab)

# find the index of the smallest distance
idx = taxicab.argmin()
print(idx, taxicab[idx])

# find the indices of the 3 smallest distances
# could use argsort
print(np.argsort(taxicab))