class Solution:
    def minOperations(self, nums: list[int]) -> int:
        
        count = 0

        i = 0
        while(i < len(nums) - 1):

            if(nums[i] >= nums[i + 1]):
                count += nums[i] + 1 - nums[i + 1]
                nums[i + 1] = nums[i] + 1
            
            i += 1

        return count