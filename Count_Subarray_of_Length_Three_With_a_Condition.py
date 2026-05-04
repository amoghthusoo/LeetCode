class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        
        ans = 0
        i = 0
        while(i < len(nums) - 2):

            if(nums[i] + nums[i + 2] == nums[i + 1]/2):
                ans += 1

            i += 1
        
        return ans