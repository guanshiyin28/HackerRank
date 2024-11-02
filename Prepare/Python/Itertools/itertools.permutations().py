# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
S, k = input().split()
[print(''.join(x)) for x in sorted(permutations(S, int(k)))]
