import numpy as np

if not np.linalg.det(np.array([[4, 6], [2, 8]])):
    print("The coefficient matrix determinant is 0.")
else:
    arr = np.linalg.solve(np.array([[4, 6], [2, 8]]), np.array([3, 7]))
    print(arr)