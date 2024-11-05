#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    
    minl = min(len(t), len(s))
    count = 0
    for i in range(minl):
        if s[i] == t[i]:
            count += 1
        else:
            break
    
    test = (k - (len(s) + len(t) - 2 * count))
    if len(s) + len(t) - 2 * count == k or (test % 2 == 0 and test >= 0) or len(s) + len(t) < k:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
