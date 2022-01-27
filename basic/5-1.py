def longestPalindrome(self, s):
    res = ""
    for i in range(len(s)):
        # odd case, like "aba"
        tmp = self.helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = self.helper(s, i, i + 1) # test
        if len(tmp) > len(res):
            res = tmp
    return res


# get the longest palindrome, l, r are the middle indexes
# from inner to outer
def helper(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1;
        r += 1
    return s[l + 1:r]


# import timeit
# x = []
# y = []
# for strlen in range(10000,100001,10000):
#     x.append(strlen)
#     y.append(timeit.timeit("x==y[1:]",setup="strlen = {}; x = '1'*strlen; y = 'a'+'1'*strlen".format(strlen)))
#     print(x[-1],y[-1])


# https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).