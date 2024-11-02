#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    previous=" "
    string=""
    for i in s:
        if previous==" ":
            l=i.upper()
            previous=i
            string+=l
            continue
        previous=i
        string+=i
    return string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
