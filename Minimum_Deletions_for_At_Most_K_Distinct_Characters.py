from collections import Counter

class Solution:
    def minDeletion(self, s: str, k: int) -> int:

        occr_dict = Counter(s)
        freq = list(occr_dict.values())

        if(k >= len(freq)):
            return 0
        else:
            freq.sort()

            to_remove = len(freq) - k
            return sum(freq[0 : to_remove])
                