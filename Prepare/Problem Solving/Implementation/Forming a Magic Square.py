#!/bin/python3

import math
import os
import random
import re
import sys
import functools
from itertools import permutations


#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
magic_squares=[]
values=[1,2,3,4,5,6,7,8,9]


def cost(t, s):
    cost=0
    for i in range(0, 3):
        for j in range(0,3):
            cost=cost+abs(t[i][j]-s[i][j])
    return cost


def list_to_matrix(list):
    return [list[ idx * 3: (idx + 1) * 3] for idx in range(0, len(list) // 3)]
    

def isMagicSquare(t):
    
    s=sum(t[0])
    for i in range(1,3):
        if sum(t[i])!=s:
            return False
    
    for i in range(0, 3):
        s1=0
        for j in range(0,3):
            s1 = s1+t[j][i] 
        if s1!=s:
            return False
    s1=0
    for i in range(0, 3):
        s1=s1+t[i][i]
    if s1!=s:
        return False
    s1=0 
    for i in range(0, 3):
        s1=s1+t[i][2-i]
    if s1!=s:
        return False
    return True


def generateSquares():
    global magic_squares
    magic_squares=[list_to_matrix(v) for v in (permutations(values)) if isMagicSquare(list_to_matrix(v)) ]


def formingMagicSquare(s):
    generateSquares()
    return min(map(lambda x: cost(x,s), magic_squares))

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
