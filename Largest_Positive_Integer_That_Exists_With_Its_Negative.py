class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        
        interList = list()

        for num in nums:
           
           if(num > 0):
               if(-num in nums):
                   interList.append(num)

        if(len(interList) != 0):
            return max(interList)

        return -1

nums = [-1,2,-3,3]
obj = Solution()
out = obj.findMaxK(nums)
print(out)