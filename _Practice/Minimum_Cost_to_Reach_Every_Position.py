class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans = []
        _min = 101

        for e in cost:
            if(e < _min):
                _min = e
            ans.append(_min)
        
        return ans