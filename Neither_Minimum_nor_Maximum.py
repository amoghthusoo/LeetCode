class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        
        if (len(nums) <= 2):
            return -1
        
        else:

            nums.sort()
            return nums[1]
        
        


nums = [2,1,3]
obj = Solution()
solution = obj.findNonMinOrMax(nums)
print(solution)