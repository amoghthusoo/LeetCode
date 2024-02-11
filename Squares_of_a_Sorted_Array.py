class Solution:
    def sortedSquares(self, nums: list) -> list:
    
        i = 0
        while (i < len(nums)):

            nums[i] = nums[i] ** 2
            i += 1

        nums.sort()

        return nums

nums = [-7,-3,2,3,11]
obj = Solution()
solution = obj.sortedSquares(nums)
print(solution)