
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)



s = input()
numRows = int(input())

sol = Solution()
answer = sol.convert(s, numRows)
print(answer)


# https://leetcode.com/problems/zigzag-conversion/discuss/3404/Python-O(n)-Solution-in-96ms-(99.43)