from collections import Counter
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        count = 0

        i = 0
        while(i <= len(s) - 3):

            occDict = dict(Counter(s[i : i + 3]))

            if(len(occDict) == 3):
                count += 1

            i += 1

        return count

s = "aababcabc"
obj = Solution()
solution = obj.countGoodSubstrings(s)
print(solution)