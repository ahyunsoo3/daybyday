class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            rst = '-' + str(x)[::-1][:len(str(x))-1]
        else:
            rst = str(x)[::-1]
        print(rst)




slv = Solution()

x = int(input())
slv.isPalindrome(x)