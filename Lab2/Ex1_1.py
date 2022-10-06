import numpy as np

arr = np.array([1, 7, 13, 105])
countbytes = arr.nbytes
print("Bytes: ", countbytes)

np.savetxt('arr1.txt', arr, fmt='%d')
arr1 = np.loadtxt('arr1.txt', dtype=int)
print("Массив из txt:", arr1)

arr.tofile('arr2.dat')
arr2 = np.fromfile('arr2.dat', dtype=int)
print("Массив из dat:", arr2)