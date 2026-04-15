from collections import Counter
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        freq_dict = Counter(nums)

        for num in nums:
            if(num % 2 == 0 and freq_dict[num] == 1):
                return num
        
        return -1