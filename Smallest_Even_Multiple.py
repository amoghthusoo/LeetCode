class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        i = n
        while(True):

            if (i % n == 0 and i % 2 == 0):
                return i
            else:
                i += 1

    
n = 6
obj = Solution()
solution = obj.smallestEvenMultiple(n)
print(solution)