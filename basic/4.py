# Given two sorted arrays num1 and num2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be 0(log (m+n)).

# num 1 + num 2 / 2


class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        return self.findKth(A, B, l // 2) if l % 2 == 1 else (self.findKth(A, B, l // 2 - 1) + self.findKth(A, B,
                                                                                                            l // 2)) / 2.0

    def findKth(self, A, B, k):
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        i = len(A) // 2
        j = k - i
        if A[i] > B[j]:
            # Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's not but in cpp it is.
            return self.findKth(A[:i], B[j:], i)
        else:
            return self.findKth(A[i:], B[:j], j)


# reference : https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2567/Python-O(log(min(mn))-solution


# Time is important, but, don't be chased it.