import random


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # 1. merged lists -> how to merge them?
        # 2. find median -> devide the size of list.

        num3 = nums1 + nums2
        num3.sort()

        if len(num3) % 2 == 0:
            temp = len(num3) // 2
            return ( num3[temp-1] + num3[temp] ) / 2

        elif len(num3) % 2 == 1:
            return num3[len(num3) // 2]

        # need my Test Case

sl = Solution()

# need to think new method of test cases

rnlist1 = random.sample(range(0, 10), 5)
rnlist2 = random.sample(range(0, 10), 5)
rnlist1.sort()
rnlist2.sort()
print(rnlist1)
print(rnlist2)


median = sl.findMedianSortedArrays(rnlist1, rnlist2)
print(median)

# Constraints:
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6