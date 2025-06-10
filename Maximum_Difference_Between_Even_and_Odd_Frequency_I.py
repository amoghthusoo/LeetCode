from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        
        occr_dict = dict(Counter(s))

        max_odd_freq = 0
        min_even_freq = int(2 ** 32 - 1)


        for freq in occr_dict.values():
            if(freq % 2 == 0):

                if(freq < min_even_freq):
                    min_even_freq = freq
            else:
                
                if(freq > max_odd_freq):
                    max_odd_freq = freq

        return max_odd_freq - min_even_freq
    
s = "aaaaabbc"
obj = Solution()
result = obj.maxDifference(s)
print(result)