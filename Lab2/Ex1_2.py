import numpy as np

arr = np.zeros(10)
arr1 = np.ones(10)
arr2 = np.zeros(10)
for i in np.arange(0, 10):
  arr2[i] = 5
print(arr)
print(arr1)
print(arr2)