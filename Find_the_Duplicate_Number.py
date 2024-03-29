class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        
        faster = nums[0]
        slower = nums[0]


        faster = nums[nums[faster]]
        slower = nums[slower]
       
        while(slower != faster):
        
            faster = nums[nums[faster]]
            slower = nums[slower]

        slower = nums[0]
        while(slower != faster):

            faster = nums[faster]
            slower = nums[slower]

        return faster
                      
        


nums = [2,5,9,6,9,3,8,9,7,1]
obj = Solution()
out = obj.findDuplicate(nums)
print(out)