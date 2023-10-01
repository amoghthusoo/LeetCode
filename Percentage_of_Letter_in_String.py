from collections import Counter
from math import floor
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        occDict = dict(Counter(s))

        try:
            return floor(occDict[letter]/len(s)*100)
        except:
            return 0

s = "sgawtb"
letter = "s"
obj = Solution()
solution = obj.percentageLetter(s, letter)
print(solution)