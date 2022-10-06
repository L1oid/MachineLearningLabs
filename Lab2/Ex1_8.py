import numpy as np

arr = np.zeros([5, 5])
np.fill_diagonal(arr, [1, 2, 3, 4, 5])
print(arr)