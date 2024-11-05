#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    li=[]
    for i in range(p , q+1):
        if(i ==1): 
            li.append(i)
                
        elif(i == 2 or i==3 ):
            continue

        elif(i>3):
            num= i*i
            digitsize = len(str(i))
            strnum=str(num)
            leftsize =  len(strnum)-digitsize
            left = int(strnum[:leftsize])
            right= int(strnum[leftsize:])
            add = left + right
            if( add == i ):
                li.append(i)
                                     
    if(len(li) >0):
        for i in range(0,len(li)):
            print(li[i] ,end=" ")
    else:
        print("INVALID RANGE") 

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
