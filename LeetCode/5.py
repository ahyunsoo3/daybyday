class qwe:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):

            tmp = self.helper(s, i, i) # There are no attributes, which affect the variable of 'i'.

            if len(tmp) > len(res):
                res = tmp
            tmp = self.helper(s, i, i + 1)


            if len(tmp) > len(res):
                res = tmp

        return res


    def helper(self, s, l, r): # the most important point in this algorithm, which means understanding this helps my knowledge of this structure.

        while l >= 0 and r < len(s) and s[l] == s[r]: # put breakpoint on this, and check out the procedure.
            l -= 1
            r += 1


        return s[l + 1:r]



# TC

qwe = qwe()
out = qwe.longestPalindrome('bbbabad')
print(out)




# Problem : https://leetcode.com/problems/longest-palindromic-substring/
# Ref : https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends).



