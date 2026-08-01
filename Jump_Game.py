class Solution:
    def canJump(self, nums: list[int]) -> bool:

        max_idx = 0
        for i in range(len(nums)):
            if(i > max_idx):
                return False

            max_idx = max(max_idx, i + nums[i])

        return True

nums = [2,3,1,1,4]
obj = Solution()
result = obj.canJump(nums)
print(result)

    