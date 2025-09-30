class Solution:
    def triangularSum(self, nums: list[int]) -> int:

        while(len(nums) != 1):
            next_arr = []
            for i in range(len(nums) - 1):
                next_arr.append((nums[i] + nums[i + 1]) % 10)
            nums = next_arr
        return nums[0]

nums = [1, 2, 3, 4, 5]
obj = Solution()
out = obj.triangularSum(nums)
print(out)