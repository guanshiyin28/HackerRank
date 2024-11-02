import numpy as np
n, m = map(int, input().split())

a = np.array([list(map(int, input().split())) for _ in range(n)])

arr_sum = list(np.sum(a, axis = 0))
result = np.prod(arr_sum)
print(result)
