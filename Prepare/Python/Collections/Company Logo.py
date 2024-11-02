#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    ch = {}

    for i in s:
        ch[i] = ch.get(i, 0) + 1
        
    sorted_by_keys = dict(sorted(ch.items()))
    sorted_by_values = dict(sorted(sorted_by_keys.items(), key=lambda item: item[1], reverse=True)[:3])

    for key, value in sorted_by_values.items():
        print(key, value)
