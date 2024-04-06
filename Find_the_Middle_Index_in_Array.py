class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        
        i = 0
        while(i < len(nums)):

            if(i == 0):
                
                if(0 == sum(nums[1 :])):
                    return 0
            
            elif(i == len(nums) - 1):

                if(sum(nums[0:len(nums) - 1]) == 0):
                    return len(nums) - 1
                
            else:

                if(sum(nums[0 : i]) == sum(nums[i + 1 : ])):
                    return i

            i += 1

        return -1
        


nums = [2,3,-1,8,4]
obj = Solution()
out = obj.findMiddleIndex(nums)
print(out)
