# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
s = input()
group = groupby(s,int)

for key, grp in group:
    print((len(list(grp)),key),end=" ")
