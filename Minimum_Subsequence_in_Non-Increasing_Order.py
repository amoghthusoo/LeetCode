class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        
        nums.sort()
        nums.reverse()

        i = 0
        while(i < len(nums)):

            if(sum(nums[0 : i + 1]) > sum(nums[i + 1 : ])):
                
                return nums[0 : i + 1]
            
            i += 1

nums = [4,4,7,6,7]
obj = Solution()
solution = obj.minSubsequence(nums)
print(solution)