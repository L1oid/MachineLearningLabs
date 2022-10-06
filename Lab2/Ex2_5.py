import numpy as np

arr = np.array([200, 300, np.nan, np.nan, np.nan, 700])
arr1 = arr[~np.isnan(arr)]
print(arr1)