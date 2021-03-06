class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
             4: 'IV', 1: 'I'}

        res = ""

        for i in d:
            res += (num // i) * d[i]
            num %= i

        return res


slv = Solution()

x = int(input())

print(slv.intToRoman(x))

# reference :
# https://leetcode.com/problems/integer-to-roman/discuss/6304/Python-simple-solution.