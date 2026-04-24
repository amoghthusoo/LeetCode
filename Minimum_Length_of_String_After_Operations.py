from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:

        ans = 0
        occr_dict = Counter(s)
        for ch, freq in occr_dict.items():
            if(freq < 3):
                ans += freq
            else:
                if(freq % 2 == 0):
                    ans += 2
                else:
                    ans += 1
        
        return ans