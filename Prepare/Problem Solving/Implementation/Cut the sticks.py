#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    Res = []
    Min = min(arr)
    Sticks = len(arr)
    while len(arr) > 0:
        Cut = 0
        while Min in arr:
            arr.remove(Min)
        for i in range(len(arr)):
            Cut += 1
            arr[i] = arr[i] - Min
        Res.append(Cut)
        if not arr:
            break
        Min = min(arr)
    Res.insert(0, Sticks)
    Res.pop()
    return Res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
