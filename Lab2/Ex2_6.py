import numpy as np

arr = np.array([1., 7., 8., 2., 0.1, 3., 15., 2.5])
arr1 = arr[np.argpartition(arr, 4)[:4]]
print(arr1)