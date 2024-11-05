#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    if "".join(sorted(w, reverse=True)) == w:
        return "no answer"
    length = len(w)
    if length == 2:
        return w[::-1]
    base_index = length -1
    while base_index > 0:
        if w[base_index] <= w[base_index-1]:
            base_index -= 1
        else:
            base_index -= 1
            break
    if base_index + 1 == length - 1:
        return w[:-2] + w[-1] + w[-2]
    result = w[:base_index]
    remainder = sorted(w[base_index:])
    base_num = w[base_index]
    highest = list(filter(lambda x: x>base_num, remainder))[0]
    remainder.remove(highest)
    result += highest + "".join(remainder)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
