import numpy as np 

a = np.arange(0,60,5)

a = a.reshape(3,4)
print('original array is:')

print(a)

print('\n')

print("modified array is: ")

for x in np.nditer(a):
    print(x)