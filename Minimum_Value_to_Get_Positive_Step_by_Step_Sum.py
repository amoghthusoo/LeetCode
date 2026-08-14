class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        total = 0
        _min = float("inf")
        for num in nums:
            total += num
            _min = min(_min, total)
        
        if(_min < 0):
            return abs(_min) + 1
        else:
            return 1