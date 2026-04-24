class Solution:
    def minCost(self, n: int) -> int:

        self.ans = 0

        def min_cost(n):
        
            if(n == 1):
                return

            left = n // 2
            right = n - left
            self.ans += (left * right)

            min_cost(left)
            min_cost(right)


        min_cost(n)
        return self.ans 


n = 3
obj = Solution()
result = obj.minCost(n)
print(result)