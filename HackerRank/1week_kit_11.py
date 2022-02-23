#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    sum = 0
    n = str(n) * k

    for i in n:
        sum += int(i)

    if len(n) != 1:
        superDigit(sum, 1)
    else:
        print(sum)



#   Or Not? : the cost of converting value of type every time seem to be highly expensive.
#    for i in n:
#        sum += int(i)




if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

