#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    arrLen = len(arr)
    sumLR = 0
    sumRL = 0

    for i in range(arrLen):
        sumLR += arr[i][i]
        sumRL += arr[i][arrLen - i - 1]

    print(abs(sumLR - sumRL))


if __name__ == '__main__':


    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
