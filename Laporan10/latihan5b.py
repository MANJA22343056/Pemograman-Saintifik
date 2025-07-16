import numpy as np

array1D = np.array([10, 20, 30, 40, 50, 60])

array1DForResize = np.array([10, 20, 30, 40])
array1DForResize.resize(2, 2)
print("Array setelah di-resize menjadi ukuran (2, 2):\n", array1DForResize)