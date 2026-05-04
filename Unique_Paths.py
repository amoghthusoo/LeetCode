from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)

m = 3
n = 7
obj = Solution()
result = obj.uniquePaths(m, n)
print(result)