class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        
        for i, num in enumerate(nums):

            num = str(num)
            _sum = 0
            for digit in num:
                _sum += int(digit)
            
            if(_sum == i):
                return i
        
        return -1