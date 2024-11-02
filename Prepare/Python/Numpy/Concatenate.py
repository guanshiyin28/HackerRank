import numpy as np

N, M, P = map(int, input().split())
A = []
B = []

for _ in range(N):
    A.append(list(map(int, input().split())))
    
for _ in range(M):
    B.append(list(map(int, input().split())))
    
ar=np.concatenate([A,B],axis=0)
print(ar)
