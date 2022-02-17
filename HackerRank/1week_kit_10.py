#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    grid = ['cba', 'eaaq', 'efa']

    for i in range(len(grid)):
        grid[i] = ''.join(sorted(grid[i]))

    print(grid)


if __name__ == '__main__':

    gridChallenge('str')

    # t = int(input().strip())
    #
    # for t_itr in range(t):
    #     n = int(input().strip())
    #
    #     grid = []
    #
    #     for _ in range(n):
    #         grid_item = input()
    #         grid.append(grid_item)
    #
    #     result = gridChallenge(grid)


# Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.
# -> The question is to do not create the grid, but identify sorted grid as ascending order in rows and columns.