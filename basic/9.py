# Given an integer x, return true if x is palindrome integer.

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x == int(str(x)[::-1]):
            return