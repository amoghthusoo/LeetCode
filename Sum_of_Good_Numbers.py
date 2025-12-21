class Solution:
    def sumOfGoodNumbers(self, nums: list[int], k: int) -> int:
        ans = 0
    
        for i in range(len(nums)):
            
            good_mem = True

            if(i - k >= 0 and nums[i] <= nums[i - k]):
                good_mem = False
            
            if(i + k < len(nums) and nums[i] <= nums[i + k]):
                good_mem = False

            if(good_mem):
                ans += nums[i]

        return ans
