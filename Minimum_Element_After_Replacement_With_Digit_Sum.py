class Solution:
    def minElement(self, nums: list[int]) -> int:
        min = int(2 ** 31) - 1
        for num in nums:
            _sum = 0
            for digit in str(num):
                _sum += int(digit)
            if(_sum < min):
                min = _sum
    
        return min

