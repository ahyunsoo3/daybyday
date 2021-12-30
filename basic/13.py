# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Given a roman numeral, convert it to an integer.

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 9


class Solution:
# @param {string} s
# @return {integer}
    def romanToInt(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1} #dictionary
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]] #is this needed?
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]
