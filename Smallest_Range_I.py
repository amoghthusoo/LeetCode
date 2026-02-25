class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        
        nums.sort()
        _min = nums[0]
        _max = nums[-1]

        diff = _max - _min

        if(diff > 2 * k):
            return diff - 2 * k
        else:
            return 0