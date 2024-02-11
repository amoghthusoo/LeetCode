class Solution:
    def findPeakElement(self, nums: list) -> int:
        
        i = 1
        while(i <= len(nums) - 2):

            if (nums[i] > nums[i - 1] and nums[i] > nums[i + 1]):
                return i
            
            i += 1

nums = [1,2,1,3,5,6,4]
obj = Solution()
solution = obj.findPeakElement(nums)
print(solution)