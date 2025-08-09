from math import log2

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if(n <= 0):
            return False
        
        l = log2(n)

        if(int(l) == l):
            return True
        else:
            return False


n = 5
obj = Solution()
result = obj.isPowerOfTwo(n)
print(result)        
