#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    Acc = 0
    Shares = 5  # Initial shares on the first day

    for _ in range(n):
        Likes = Shares // 2  # Calculate likes as half of the shares
        Acc += Likes  # Accumulate the total likes
        Shares = Likes * 3  # Calculate new shares based on the likes

    return Acc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
