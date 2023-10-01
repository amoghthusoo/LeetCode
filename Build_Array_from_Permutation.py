class Solution:
    def buildArray(self, nums: list) -> list:

        return [nums[nums[i]] for i in range(len(nums))]

nums = nums = [5,0,1,2,3,4]
obj = Solution()
solution = obj.buildArray(nums)
print(solution)