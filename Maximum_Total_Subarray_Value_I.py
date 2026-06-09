class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        
        _min, _max = nums[0], nums[0]

        for num in nums:

            if(num < _min):
                _min = num
            
            if(num > _max):
                _max = num

        
        return (_max - _min) * k