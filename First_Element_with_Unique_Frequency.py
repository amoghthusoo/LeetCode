from collections import Counter
class Solution:
    def firstUniqueFreq(self, nums: list[int]) -> int:
        
        occr_dict = Counter(nums)
        freqs = occr_dict.values()
        freq_dict = Counter(freqs)

        for num in nums:

            freq = occr_dict[num]

            if(freq_dict[freq] == 1):
                return num
            
        return -1

