class Solution:
    def minCosts(self, cost: list[int]) -> list[int]:
        
        ans = []
        _min = 101

        for e in cost:
            if(e < _min):
                _min = e
            ans.append(_min)
        
        return ans
    
cost = [1,2,4,6,7]
obj = Solution()
result = obj.minCosts(cost)
print(result)
