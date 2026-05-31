class Solution:
    def subarraySum(self, nums: list[int]) -> int:
        
        ans = 0
        for i, e in enumerate(nums):
            start = max(0, i - e)
            end = i + 1
            ans += sum(nums[start : end])
        
        return ans