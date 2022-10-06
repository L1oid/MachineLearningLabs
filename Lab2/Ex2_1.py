import numpy as np

arr1 = [0, 10, 20, 40, 60]
arr2 = [10, 30, 40]
arr = np.intersect1d(arr1, arr2)
print(arr)