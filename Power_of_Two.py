class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        i = 0

        while True:

            if (2 ** i == n):
                return True
            elif (2 ** i > n):
                return False
            
            i += 1

n = 16
obj = Solution()
solution = obj.isPowerOfTwo(n)
print(solution)