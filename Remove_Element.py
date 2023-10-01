class Solution:
    def removeElement(self, nums: int, val: int) -> int:
        
        while (val in nums):
            del(nums[nums.index(val)])
        
        return len(nums), nums

nums = [0,1,2,2,3,0,4,2]
val = 2
obj = Solution()
solution, nums = obj.removeElement(nums, val)
print(solution, nums)