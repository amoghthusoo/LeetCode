from collections import Counter
from itertools import permutations

class Solution:

    def seq_repeated_k_times(self, small, large, k):

        it = iter(large)
        for _ in range(k):
            if(not all(ch in it for ch in small)):
               return False
        return True

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        
        freq_dict = Counter(s)

        intr_arr = []

        for ch, freq in freq_dict.items():
            intr_arr.extend([ch for _ in range(freq // k)])

        intr_arr.sort(reverse = True)

        r = len(intr_arr)

        seen = set()
        while(r >= 0):

            it = permutations(intr_arr, r)

            for cand in it:
                cand = "".join(cand)
                if(cand not in seen):
                    seen.add(cand)
                    if(self.seq_repeated_k_times(cand, s, k)):
                        return cand
            r -= 1

        return ""

from time import time
start = time()
s = "oqswqmtewpwwqwygbwqjwsqrwqwqlxwhqwcqwxqwqfwxqqwqjrwjewqwqqwqibwqyewpqwqwvqwqwqlwoqwqlgwpqgcwqzzyiqwqwqwqkyrwkuqwqztcwlqwzerdqqewpvqwfqwqwqwoxqwqwqwqwqryagwwqwwqvwdqqwqwfqwcqwqwqwxqwqwpqspqwqwqwqwqwrqewqffvnwhlqtiwqwyqwiqqjwqwchyqwwqwqqwwqwmqzrwgquweosquwlquwaqwqwkwcqwqfwdpqwqcwqwifucqwqtwqewqcylgwqwyqwqwptqfwfqwqwbqwqijqwqwaqkuzwukqwswklmzqwwozqwqjwqdqwqwqwqcwqmqw"
k = 102
obj = Solution()
result = obj.longestSubsequenceRepeatedK(s, k)
print(result)
end = time()
print(end - start)