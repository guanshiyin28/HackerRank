# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

name, k = input().split()
name = sorted(name)

print(*list("".join(i) for i in sorted(combinations_with_replacement(name, int(k)))), sep="\n")
