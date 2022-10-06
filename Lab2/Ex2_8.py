import numpy as np

arr1 = ['Python', 'PHP']
arr2 = ['Java', 'C ++']
arr = np.apply_along_axis(' '.join, 0, [arr1, arr2])
print(arr)