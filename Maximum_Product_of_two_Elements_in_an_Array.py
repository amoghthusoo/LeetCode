class Solution:
    def maxProduct(self, nums: list) -> int:
        
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)


nums = [3,7]
obj = Solution()
solution = obj.maxProduct(nums)
print(solution)