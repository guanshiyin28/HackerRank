# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations as com
l,p = input().split()
l = sorted(l)
for i in range(int(p)):
    b = list(com(l,(int(i) + 1)))
    for k in b:
        print(''.join(k))
