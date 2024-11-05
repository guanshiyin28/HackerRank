#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    n = len(topic)
    l = len(topic[0])
    
    hashmap = {}
    for i in range(n):
        for j in range(i + 1, n):
            result = 0
            for k in range(l):
                if topic[i][k] == '1' or topic[j][k] == '1':
                    result += 1
            hashmap[result] = 1 + hashmap.get(result, 0)
             
    max_result = max(hashmap.keys())
    
    return max_result, hashmap[max_result]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
