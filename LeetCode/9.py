class Solution:
    # @param x, an integer
    # @return a boolean
    def isPalindrome(self, x):
        return False if x < 0 else str(x) == str(x)[::-1]


# Reference :
# https://leetcode.com/problems/palindrome-number/discuss/1795376/python-oneliner