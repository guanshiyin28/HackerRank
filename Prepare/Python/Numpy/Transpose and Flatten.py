import numpy as np

N, M = map(int, input().split())
elements=[]

for _ in range(N):
    elements.append(list(map(int, input().split())))

array = np.array(elements)
print(array.transpose())
print(array.flatten())
