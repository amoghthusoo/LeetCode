class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        max_sum = -int(2 ** 31)
        current_sum = 0

        i = 0
        while(i < len(nums)):

            current_sum += nums[i]

            if(current_sum > max_sum):
                max_sum = current_sum

            if(current_sum < 0):
                current_sum = 0

            i += 1

        return max_sum

nums = [-2,-1]
obj = Solution()
out = obj.maxSubArray(nums)
print(out)