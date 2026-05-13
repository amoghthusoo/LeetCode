class Solution:
    def alternatingSum(self, nums: list[int]) -> int:
        
        ans = 0
        for i, e in enumerate(nums):
            if(i % 2 == 0):
                ans += e
            else:
                ans -= e
        return ans