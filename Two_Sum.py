class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        
        i = 0
        while (i < len(nums)):
            j = i + 1
            while (j < len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
                j += 1
            i += 1




nums = [2,7,11,15] 
target = 9
obj = Solution()
solution = obj.twoSum(nums, target)
print(solution)