from math import gcd
class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        ans = []

        for d in range(2, n + 1):
            for n in range(1, d):
                if(gcd(n, d) == 1):
                    ans.append(f"{n}/{d}")
        
        return ans
    
n = 4
obj = Solution()
result = obj.simplifiedFractions(n)
print(result)