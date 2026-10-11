class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        
        n = len(nums)

        _sum = 0
        for i in range(n):

            if (n % (i + 1) == 0):
                _sum += nums[i] ** 2
        
        return _sum