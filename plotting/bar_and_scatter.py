import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2)

# a bar chart in the top-left axis
ax[0, 0].bar(x=['canada', 'usa', 'russia'], height=[1, 2, 3], width=0.8)


# a scatter plot in the bottom-right axis
ax[1,1].scatter(x=[1, 2, 2, 4, 4], y=[1, 2, 3, 4, 5])
ax[1,1].scatter(x=[1, 2, 3, 3, 5], y=[2, 2, 2, 1, 0])
ax[1, 1].set_xlabel('(the x axis label)')
ax[1, 1].set_ylabel('(the y axis label)')
ax[1,1].set_title('a scatter plot')
ax[1, 1].legend(['series A', 'series B'])
ax[1,1].set_xticks([1, 2, 3, 4])
ax[1, 1].set_xticklabels(['one', 'two', 'three', 'four'])

plt.tight_layout()
plt.show()