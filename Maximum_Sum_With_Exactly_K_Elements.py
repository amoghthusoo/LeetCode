class Solution:
    def maximizeSum(self, nums: list, k: int) -> int:
        
        n = max(nums)
        maxScore = int(((n + k)*(n + k - 1) - n * (n - 1)) / 2)
        return maxScore


nums = [5,5,5]
k = 2
obj = Solution()
solution = obj.maximizeSum(nums, k)
print(solution)