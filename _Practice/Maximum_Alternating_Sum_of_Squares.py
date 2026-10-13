class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        for i, e in enumerate(nums):
            nums[i] = abs(e)
        
        nums.sort()

        if(len(nums) % 2 == 0):
            k = len(nums) // 2
        else:
            k = (len(nums) - 1) // 2

        
        ans = 0
        for i in range(k):
            ans += -nums[i] * nums[i]
        
        for i in range(k, len(nums)):
            ans += nums[i] * nums[i]

        return ans