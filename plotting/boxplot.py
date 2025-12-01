import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

ax.boxplot([1, 2, 3, 4, 4, 3, 4, 5, 6, 10])

plt.show()