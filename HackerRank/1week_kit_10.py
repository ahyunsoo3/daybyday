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

def gridChallenge(gridStr):



    lenGrid = len(gridStr)
    lenEle = len(gridStr[0])
    grid = []
    # making elements of grid being list.
    for i in range(lenGrid):
        grid.append(list(gridStr[i]))


    #rearrange only rows
    for i in range(lenGrid):
        for j in range(lenEle):
            for k in range(j+1, lenEle):
                if grid[i][j] > grid[i][k]:
                    temp = grid[i][j]
                    grid[i][j] = grid[i][k]
                    grid[i][k] = temp



    #determine
    for i in range(lenGrid):
        for j in range(lenEle):
            if j == lenEle - 1: break
            elif grid[i][j] > grid[i][j+1]:
                print ("NO")
                return

    for j in range(lenEle):
        for i in range(lenGrid):
            if i == lenGrid - 1: break
            elif grid[i][j] > grid[i+1][j]:
                print ("NO")
                return

    print("YES")
    return









if __name__ == '__main__':


    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)


# Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.
# -> The question is to do not create the grid, but identify sorted grid as ascending order in rows and columns. [x]
# -> rearrange & determine [o]