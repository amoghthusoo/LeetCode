from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        occDict : dict = dict(Counter(s))
        indexList : list = []

        for key, value in occDict.items():

            if (value == 1):
                indexList.append(s.index(key))
        
        indexList.sort()

        if (len(indexList) != 0):
            return indexList[0]
        else:
            return -1

s = "aabb"
obj = Solution()
solution = obj.firstUniqChar(s)
print(solution)
