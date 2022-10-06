import numpy as np

arr = ['Python', 'PHP', 'JS', 'examples', 'html']
arr1 = np.char.count(arr, 'P')
print(arr1)