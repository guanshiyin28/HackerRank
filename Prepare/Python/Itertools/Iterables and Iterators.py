# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
N = int(input())
A = list(input().split())
K = int(input())
B = list(combinations(A, K))
count = sum(1 for x in B if 'a' in x)
print(count/len(B))
