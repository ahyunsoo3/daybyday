#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    sol = [0] * 100
    for a in arr:
        sol[a] += 1

    print (*sol, sep=' ')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)


# - Reference -
# 1. solution
# https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/forum?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two
# 2. without the brackets, commas
# https://stackoverflow.com/questions/17757450/how-to-print-a-list-with-integers-without-the-brackets-commas-and-no-quotes/17757544
