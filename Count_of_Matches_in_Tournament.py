class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        if(n == 1):
            return 0

        if(n % 2 == 0):
            return n//2 + self.numberOfMatches(n//2)
        else:
            return n//2 + self.numberOfMatches(n//2 + 1)

n = 14
solution = Solution()
result = solution.numberOfMatches(n)
print(result)
