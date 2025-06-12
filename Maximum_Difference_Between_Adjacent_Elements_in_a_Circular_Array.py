class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        
        max_diff = -1

        i = 0
        while(i < len(nums)):
            
            diff = abs(nums[i] - nums[i - 1])
            
            if(diff > max_diff):
                max_diff = diff
            
            i += 1

        return max_diff
    
nums = [1,2,4]
obj = Solution()
result = obj.maxAdjacentDistance(nums)
print(result)