# Given an integer x, return true if x is palindrome integer.

class Solution:
    def isPalindrome(self, x):
        return False if x < 0 else x == int(str(x)[::-1])
