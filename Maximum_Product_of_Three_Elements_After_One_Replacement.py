class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        for i, e in enumerate(nums):
            nums[i] = abs(e)

        nums.sort()
        return abs(nums[-1]) * abs(nums[-2]) * 100000