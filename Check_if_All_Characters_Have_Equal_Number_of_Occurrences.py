from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        occDict = dict(Counter(s))
        occOccDict = dict(Counter(list(occDict.values())))

        if (len(occOccDict) == 1):
            return True
        else:
            return False

s = "abacbc"
obj = Solution()
solution = obj.areOccurrencesEqual(s)
print(solution)