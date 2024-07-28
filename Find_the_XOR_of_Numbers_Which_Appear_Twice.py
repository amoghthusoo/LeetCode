from collections import Counter

class Solution:
    def duplicateNumbersXOR(self, nums: list[int]) -> int:
        
        occr_dict = dict(Counter(nums))

        out = 0

        for key, value in occr_dict.items():

            if(value == 2):
                out ^= key

        return out
