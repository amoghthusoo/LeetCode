class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        
        if (target not in nums):
            return [-1, -1]
        else:
            ansList = []
            ansList.append(nums.index(target))
            nums.reverse()
            ansList.append(len(nums) - 1 -nums.index(target))

            return ansList

nums = [5,7,7,8,8,10]
target = 8
obj = Solution()
solution = obj.divide(nums, target)
print(solution)