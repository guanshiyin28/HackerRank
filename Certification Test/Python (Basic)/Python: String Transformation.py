#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()
