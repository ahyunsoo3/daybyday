class Solution:
    def isPalindrome(self, x: int) -> bool:
        rst = str(x)[::-1]
        if x < 0: return False
        elif int(rst) == x: return True






slv = Solution()

x = int(input())
slv.isPalindrome(x)