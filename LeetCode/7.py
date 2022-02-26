class Solution:
    def reverse(self, x: int) -> int:
        vstr = list(str(x))
        strLen = len(vstr)




        for i in range(0, strLen):
            if vstr[i] != '-':
                if (strLen-1) // 2 == i and strLen != 2:
                    break
                else:
                    temp = vstr[i]
                    if strLen != 2:
                        vstr[i] = vstr[strLen - i - 1]
                        vstr[strLen - i - 1] = temp
                    else:
                        vstr[i] = vstr[strLen - 1]
                        vstr[strLen - 1] = temp
            else:
                i += 1
                if (strLen-1) // 2 == i and strLen != 2:
                    break
                else:
                    temp = vstr[i]
                    vstr[i] = vstr[strLen - i]
                    vstr[strLen - i - 1] = temp

        vstr = ''.join(vstr)
        print(vstr)


slv = Solution()

x = int(input())
slv.reverse(x)