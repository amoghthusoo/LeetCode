from collections import Counter
class Solution:
    def sumDivisibleByK(self, nums: list[int], k: int) -> int:
        
        freq_dict = Counter(nums)

        ans = 0
        for num, freq in freq_dict.items():
            if(freq % k == 0):
                ans += num * freq
        return ans