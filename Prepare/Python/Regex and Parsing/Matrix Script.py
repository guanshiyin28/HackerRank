#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
decode = list(zip(*matrix))
decode_string = "".join(map(lambda string: "".join(string), decode))

pattern = re.compile(r"((?<=\w)([!@#$%&\s]+)(?=\w))|\s\s")
neo = re.sub(pattern, " ", decode_string)
print(neo)
