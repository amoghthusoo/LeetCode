from collections import Counter
class Solution:
    def arrayRankTransform(self, arr: list) -> list:
        
        interArr = [i for i in arr]

        interArr.sort()

        occDict = dict(Counter(interArr))
        occDictKeys = list(occDict.keys())
        rankDict = {}

        i = 0
        while (i < len(occDictKeys)):

            rankDict[occDictKeys[i]] = i + 1
            i += 1

        ansList = []

        for element in arr:
            ansList.append(rankDict[element])

        return ansList

        



arr = [37,12,28,9,100,56,80,5,12]
obj = Solution()
solution = obj.arrayRankTransform(arr)
print(solution)