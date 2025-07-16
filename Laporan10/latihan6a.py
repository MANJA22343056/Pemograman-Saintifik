import numpy as np

array2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

array1D = np.array([10, 20, 30])

result = array2D + array1D

print("array 2D asli:\n", array2D)
print("array 1D yang akan ditambahkan:\n", array1D)
print("hasil penambahan array 1D ke setiap baris array 2D:\n", result)