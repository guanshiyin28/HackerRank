# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
res = deque()
for i in range(int(input())):
    u = input().split()
    if not hasattr(res, u[0]):
        continue
    val = u[1] if len(u) > 1 else None
    if val:
        getattr(res, u[0])(val)
    else:
        getattr(res, u[0])()
print(*res)
