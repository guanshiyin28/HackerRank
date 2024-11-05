#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # (s = aba, n = 10) -> abaabaabaa
    
    c1 = s.count('a')  # no. of a's in string (aba) -> 2
    cf = c1 * (n // len(s))
    # no. of total a's except last iteration (aba aba aba) -> 6
    
    fchar = n % len(s)
    # reamining part of the specified string -> 10 % len(aba) -> 1
    
    i = s[0 : fchar] # gettng the remaining string -> s[0:1] -> 'a'
    
    cf += i.count('a') # no. of a's in remaing string -> 'a'.count(a) -> 1
    
    return cf # 7

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
