from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        
        multiplier = 1
        freq = sorted(list(dict(Counter(word)).values()), reverse= True)
        
        presses = 0
        i = 0
        for f in freq:
            presses += f * multiplier
            i += 1
            if(i == 8):
                multiplier += 1
                i = 0

        return presses

word = "abcde"
solution = Solution()
result = solution.minimumPushes(word)
print(result)