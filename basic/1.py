class Solution:
    #original
    #def twoSum(self, nums: List[int], target: int) -> List[int]:

    def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):


# 1 2 3 4 / 5

# 2+3 = 5
# 1+4 = 5
# The soultion want exactly one solution. So, I need just one.


                if nums[j] == target - nums[i]:
                    return [i, j]





sol = Solution

res = sol.twoSum(nums=[1,2,3,4], target=5)

print(res)
