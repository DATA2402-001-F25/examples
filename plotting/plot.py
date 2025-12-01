import matplotlib.pyplot as plt


fig, ax = plt.subplots(nrows=1, ncols=2)
# ax is a single Axes object if nrows == ncols == 1
# it's a numpy array of Axes objects otherwise

# do a lineplot in the "left" axes
ax[0].plot([1, 2, 1, 3])

# do another one in the 'right" axes
ax[1].plot([1, 2, 4, 8], [1, 2, 1, 3], color='red', linestyle=':', marker='o')


plt.show()
print('done')  # note this line doesn't run until plot is closed
