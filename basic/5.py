# Given a string s, return the longest palindromic substring in s.
# palindrome : a word or phrase that reads the same backwards as forwards

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s)==0:
        	return 0
        maxLen=1
        start=0
        for i in xrange(len(s)):
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue

        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen]


# https://leetcode.com/problems/longest-palindromic-substring/discuss/2925/Python-O(n2)-method-with-some-optimization-88ms.



