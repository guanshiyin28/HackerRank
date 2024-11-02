import numpy as np

n = list(map(int, input().split()))
arr = np.array(n)
print(arr.reshape(3,3))
