import numpy as np
import pandas as pd

arr = np.array([[0, 1], [2, 3]])
stacked = np.concatenate([arr, arr, arr], axis=0)
print(stacked)

