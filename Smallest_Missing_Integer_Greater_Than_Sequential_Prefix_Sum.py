class Solution:
    def missingInteger(self, nums: list[int]) -> int:

        total = nums[0]
        i = 1
        while(i < len(nums) and nums[i - 1] + 1 == nums[i]):
            total += nums[i]
            i += 1

        nums_set = set(nums)
        while(total in nums_set):
            total += 1
        return total

nums = [1,2,3,2,5]
obj = Solution()
result = obj.missingInteger(nums)
print(result)