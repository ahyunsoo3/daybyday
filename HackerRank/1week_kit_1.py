#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):

    pos_pos = 0
    pos_neg = 0
    pos_zero = 0
    len_arr = len(arr)
    for i in range(len(arr)):
        if arr[i] == 0:
            pos_zero += 1 / len_arr
        elif arr[i] < 0:
            pos_neg += 1 / len_arr
        elif arr[i] > 0:
            pos_pos += 1 / len_arr

    print(pos_pos)
    print(pos_neg)
    print(pos_zero)


if __name__ == '__main__':
    # n = int(input().strip())
    #
    # arr = list(map(int, input().rstrip().split()))

    arr = [1,5,3,-1,0,-2]
    plusMinus(arr)
