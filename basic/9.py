# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 else x == int(str(x)[::-1])

        # Why Leetcode has only few cases? I am annoying that this solution must be the most efficient one.