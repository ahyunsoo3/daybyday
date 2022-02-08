import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hh = s[:2]
    mm = s[3:5]
    ss = s[6:8]

    if s[-2:] == 'PM':
        hh = int(hh) + 12

    print(f"{hh}:{mm}:{ss}")




if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

