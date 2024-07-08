class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        
        i = 1
        while(True):

            if("0" in str(n - i) or "0" in str(i)):
                i += 1
            else:
                return [i, n - i]

n = 11
obj = Solution()
out = obj.getNoZeroIntegers(n)
print(out)     