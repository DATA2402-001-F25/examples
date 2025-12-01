import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

ax.hist([1, 2, 3, 4, 4, 3, 4, 5, 6, 10], bins=[0, 1, 5, 7, 11])

plt.show()