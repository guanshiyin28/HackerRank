# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
K, M = map(int, input().split())
A = [None]*K
B = [None]*K
for x in range(K):
    A[x], B[x] = input().split(' ', 1)
    B[x] = list(map(int, B[x].split()))
SQ = [[v ** 2 for v in B[x]] for x in range(K)]
MT = max((sum(x)%M for x in product(*SQ)), default = 0)
print(MT)
