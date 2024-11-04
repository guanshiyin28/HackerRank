#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    
    ranked = sorted(set(ranked), reverse=True)
    rankFinal: list = []
    #print(ranked)
    
    for ply in player:
        for rankPos, rankScore in enumerate(ranked, 1):
            if ply >= rankScore:
                #print(ply, rankPos, rankScore)
                rankFinal.append(rankPos)
                break
            if rankPos == len(ranked):
                #print(ply, rankPos+1)
                rankFinal.append(rankPos+1)
    
    return rankFinal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
