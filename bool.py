import numpy as np

arr = np.arange(12).reshape(3,4)

print(arr)

print(' ')
b = arr>5

print(b)
print(b.dtype)