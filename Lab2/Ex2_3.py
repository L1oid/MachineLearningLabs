import numpy as np

arr = [10, 10, 20, 10, 20, 20, 20, 30, 30, 50, 40, 40]
arr1 = np.unique(arr)
arr2 = arr1.searchsorted(arr)
arr3 = np.bincount(arr2)
print(arr1)
print(arr3)