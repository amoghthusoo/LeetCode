from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:

        s_map = Counter(s)
        target_map = Counter(target)

        for ch in target_map:

            if(ch not in s_map):
                return 0

            s_map[ch] //= target_map[ch]

        target_letters = set(target)
        inter_ans = []


        for ch, freq in s_map.items():
            if(ch in target_letters):
                inter_ans.append(freq)

        return min(inter_ans)        
         