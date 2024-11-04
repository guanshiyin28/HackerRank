#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    
    numList = sorted(a)
    score = 0

    start = 0
    end = 1
    
    while end < len(numList):
        
        if numList[end] - numList[start] < 2:
            end += 1
            score = max(score , end - start)
        else:
            start += 1

    return score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
