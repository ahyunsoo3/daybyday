# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

import random

class Solution:

    def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]: # it is just transition.
                    return [i, j]


sol = Solution
sp = random.sample(range(0,10), 5)
res = sol.twoSum(nums = sp, target = 5)

print(sp)
print('-------------------')
print(res)
