class Solution:
    def minOperations(self, nums):
        
        count = 0
        i = 0
        while(i < len(nums) - 2):
            
            if(nums[i] == 0):
                nums[i] = 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                count += 1
            i += 1

        if(nums[i] == 0 or nums[i + 1] == 0):
            return -1
        else:
            return count

nums = [0,1,1,1]
solution = Solution()
result = solution.minOperations(nums)
print(result)