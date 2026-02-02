class Solution:
    def minimumPrefixLength(self, nums: list[int]) -> int:
        
        i = len(nums) - 1
        while(i > 0):

            if(nums[i - 1] >= nums[i]):
                break

            i -= 1
        
        return i
    
nums = [1,2,3,4]
obj = Solution()
result = obj.minimumPrefixLength(nums)
print(result)