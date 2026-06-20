class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        
        lb = n - k
        ub = n + k

        lb = max(0, lb)

        ans = 0
        for x in range(lb, ub + 1):
            if(n & x == 0):
                ans += x

        return ans