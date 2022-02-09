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
    meridiem = s[-2:]

    if hh == '12' and meridiem == 'AM':
        hh = '00'
    elif meridiem == 'PM' and hh != '12':
        hh = int(hh) + 12

    print(f"{hh}:{mm}:{ss}")




if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

