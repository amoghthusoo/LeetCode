class Solution:
    def mySqrt(self, x: int) -> int:
        
        i = 1
        while (True):
            
            if (i * i) > x:
                return i - 1
            
            i += 1

x = 8
obj = Solution()
solution = obj.mySqrt(x)
print(solution)