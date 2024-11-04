#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    aux, aux2 = 0, 0 
    list =[] 
    for i in range(0, n+1, 2):
        list.append([i,i+1])

    for i in range(len(list)):
        if p in list[i]:
            aux = i
    
    for num, i in enumerate(reversed(list)):
        if p in i:
            aux2 = num

    if aux < aux2:
        return aux
    else:
        return aux2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
