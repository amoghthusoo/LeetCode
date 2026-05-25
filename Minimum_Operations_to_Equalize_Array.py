from collections import Counter
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        
        freq_dict = Counter(nums)

        if(freq_dict[nums[0]] == len(nums)):
            return 0
        else:
            return 1
