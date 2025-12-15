class Solution:
    def absDifference(self, nums: list[int], k: int) -> int:
        
        nums.sort()
        return abs(sum(nums[0 : k]) - sum(nums[-k : ]))