class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        
        count = 0
        while(count < k):
            nums[nums.index(min(nums))] *= multiplier            
            count += 1

        return nums