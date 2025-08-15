from math import log, isclose

class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if(n <= 0):
            return False
        
        l = log(n, 4)
        if(isclose(l, round(l), rel_tol = 0.000000000001)):
            l = round(l)

        if(int(l) == l):
            return True
        else:
            return False


n = 129140162
obj = Solution()
result = obj.isPowerOfTwo(n)
print(result)        
