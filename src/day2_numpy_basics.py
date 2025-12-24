import numpy as np

z = np.arange(10,30)
z = z[::-1]
idx = np.nonzero(z)

arr = z[idx]
print(arr.shape, arr.size)