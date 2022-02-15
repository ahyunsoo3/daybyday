#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    k = k % 26
    lis = list(s)
    for i in range(len(s)):
        if 65 <= ord(lis[i]) <= 90:
            if 90 < ord(lis[i]) + k:
                lis[i] = chr(ord(lis[i]) + k - 26)
            else:
                lis[i] = chr(ord(lis[i]) + k)
        elif 97 <= ord(lis[i]) <= 122:
            if 122 < ord(lis[i]) + k:
                lis[i] = chr(ord(lis[i]) + k - 26)
            else:
                lis[i] = chr(ord(lis[i]) + k)

    s = ''.join(lis)
    print(s)

if __name__ == '__main__':

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

