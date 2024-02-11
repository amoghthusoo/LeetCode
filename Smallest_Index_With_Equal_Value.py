class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        
        i = 0
        while(i < len(nums)):
            
            if(i % 10 == nums[i]):
                return i
                    
            i += 1

        return -1

nums = [4,3,2,1]
obj = Solution()
solution = obj.smallestEqual(nums)
print(solution)