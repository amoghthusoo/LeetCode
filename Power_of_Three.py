import math 
class Solution:
    def isPowerOfFour(self, n: int) -> bool:


        try:
            exponent = math.log(n, 3)

            try:
                if (".99999999999999" in str(exponent) or 
                    ".99999999999999" in str(exponent) or
                    ".99999999999999" in str(exponent)):      
                    return True
            except:
                pass

            if (str(exponent)[-2:] == ".0"):
                return True
            else:
                return False
            
        except:
            return False

n = 129140163
obj = Solution()
solution = obj.isPowerOfFour(n)
print(solution)


"""
exceptional numbers :
243
59049
"""