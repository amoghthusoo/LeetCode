import math 
class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        try:
            exponent = math.log(n, 4)
            if (str(exponent)[-2:] == ".0"):
                return True
            else:
                return False
            
        except:
            return False

n = 0
obj = Solution()
solution = obj.isPowerOfFour(n)
print(solution)