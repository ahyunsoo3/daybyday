class Solution:
    def median(self, nums1, nums2):
        # 1. merged lists -> how to merge them?
        # 2. find median -> devide the size of list.

        integ = nums1 + nums2
        if len(integ) % 2 == 0:
            temp = len(integ) // 2
            return ( integ[temp-1] + integ[temp] ) / 2
        elif len(integ) % 2 == 1:
            return integ[len(integ)] / 2

        # need my Test Case

sl = Solution()

# need to think new method of test cases
median = sl.median([1,2,3], [4,5,6])
print (median)