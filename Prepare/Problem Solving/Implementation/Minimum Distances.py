#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    dist = float('inf')
    for i in range(len(a)):
        if a[i] in a[i+1:]:
            b = a.index(a[i],i+1,len(a))
            dist = min(dist,abs(i-b))
    if dist == float('inf'):
        return -1 
    else:
        return dist

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
