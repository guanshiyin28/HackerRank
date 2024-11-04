#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    lis = []
    farr = set(arr)
    for i in farr:
        count = 0
        for j in arr:
            if(i == j):
                count+=1
        lis.append([i,count])
    s_list = sorted(lis, key=lambda x: x[1],reverse=True)
    f_list = []
    for k in range(len(s_list)-1):
        if(k==0):
            f_list.append(s_list[k])
        elif(s_list[k][1]==s_list[k+1][1]):
            f_list.append(s_list[k+1])
        if(s_list[k][1]>s_list[k+1][1]):
            break
    fin_list= sorted(f_list,key=lambda x: x[0])
    return fin_list[0][0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
