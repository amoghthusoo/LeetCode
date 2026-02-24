from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums: list[int]) -> bool:

        freq_arr = Counter(nums)

        for num, freq in freq_arr.items():
            if(freq > 2):
                return False
        
        return True
