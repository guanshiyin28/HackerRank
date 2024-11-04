#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    time = s[-2:]
    hour = int(s[:2])
    final_time = s[:-2]
    if time == 'AM':
        if hour==12:
            final_time = '00'+s[2:-2]
        
    else:
        if hour < 12:
            new_hour = 12+hour
            final_time = str(new_hour)+s[2:-2]
    return final_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
