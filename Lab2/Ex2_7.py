import numpy as np

arr = np.array([0.5, 1.8, 2.1, 3.5, 4.87, 5.13, 6.49])
i = (np.abs(arr - 3.09066280756759)).argmin()
print(arr[i])