import math
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        
        mod = 10 ** 9 + 7
        powers = []
        i = 1
        while(True):

            pow = int(i ** x)
            if(pow <= n):
                powers.append(pow)
            else:
                break
            i += 1
        
        dp = [[None for _ in range(n + 1)] for _ in range(len(powers))]

        dp[0][0] = 1
        dp[0][1] = 1
        for j in range(2, len(dp[0])):
            dp[0][j] = 0
        

        i = 1
        while(i < len(dp)):

            j = 0
            while(j < len(dp[0])):

                if(j < powers[i]):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - powers[i]]) % mod

                j += 1
            i += 1

        return dp[-1][-1]

n = 64
x = 3
obj = Solution()
result = obj.numberOfWays(n, x)
print(result)