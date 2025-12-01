import matplotlib.pyplot as plt
import numpy as np


vals = np.random.normal(loc=0, scale=1, size=1000)
vals[-1] = 99  # an outlier value


fig, ax = plt.subplots(1, 1)
ax.hist(vals, bins=[-float('inf'), -3, -2, -1, 0, 1, 2, 3, float('inf')])
ax.set_xticks([-4, -3, -2, -1, 0, 1, 2, 3, 4])
ax.set_xlim([-4, 4])
ax.set_xticklabels(['<-4', '-3', '-2', '-1', '0', '1', '2', '3', '>4'])

plt.show()