# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.

import random


class Solution:

    def two_sum(self, nums : list, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]: #math
                    return [i, j]


sol = Solution
sp = random.sample(range(0, 10), 5) # list: 5
res = sol.two_sum

print(sp)
print('-------------------')
print(res)


# PEP 8 -- Style Guide for Python Code
# Python Enhancement Proposal


# Why does pycharm propose to change method to static
# https://stackoverflow.com/questions/23554872/why-does-pycharm-propose-to-change-method-to-static
