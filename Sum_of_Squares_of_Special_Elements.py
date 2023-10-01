class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        
        n = len(nums)

        _sum = 0
        for i in range(n):

            if (n % (i + 1) == 0):
                _sum += nums[i] ** 2
        
        return _sum




nums = [2,7,1,19,18,3]
obj = Solution()
solution = obj.sumOfSquares(nums)
print(solution)