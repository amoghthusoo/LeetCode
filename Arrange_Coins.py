from math import sqrt
class Solution:
    def arrangeCoins(self, n: int) -> int:

        def positiveRoot(n):
            k = (sqrt(8 * n + 1) - 1) / 2
            return k
        
        while True:

            k = positiveRoot(n)
            if str(k)[-2:] == ".0":
                return int(k)
                
            n -= 1        



n = 8
obj = Solution()
solution = obj.arrangeCoins(n)
print(solution)