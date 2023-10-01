# NOT SOLVED
from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list:

        s1 = s1.split()
        s2 = s2.split()

        s1occDict = dict(Counter(s1))
        s2occDict = dict(Counter(s2))

        s1 = []
        s2 = []

        for key in s1occDict:
            
            if s1occDict[key] == 1:
                s1.append(key)
        
        for key in s2occDict:
            
            if s2occDict[key] == 1:
                s2.append(key)

        ansList = []

        for word in s1:

            if word not in s2:
                ansList.append(word)

        for word in s2:
            
            if word not in s1:
                ansList.append(word)

        ansList = list(dict(Counter(ansList)).keys())

        return ansList

s1 = "s z z z s"
s2 = "s z ejt"
obj = Solution()
solution = obj.uncommonFromSentences(s1, s2)
print(solution)