class Solution:
    def maxProductDifference(self, nums: list[int]) -> int:
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])

nums = [4,2,5,9,7,4,8]
obj = Solution()
solution = obj.maxProductDifference(nums)
print(solution)