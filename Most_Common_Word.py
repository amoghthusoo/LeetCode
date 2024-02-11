from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list) -> str:

        wordList = []

        i = 0
        j = 0
        spaceMem = False

        while (i < len(paragraph)):

            if (i == 0):
                wordList.append(paragraph[i])
            elif (paragraph[i] in ["!", "?", "'", ",", ";", ".", " "]):
                spaceMem = True
            elif (spaceMem):
                wordList.append(paragraph[i])
                spaceMem = False
                j += 1
            else:
                wordList[j] += paragraph[i]
                
            i += 1

        i = 0
        while (i < len(wordList)):
            wordList[i] = wordList[i].lower()
            i += 1

        i = 0
        while (i < len(banned)):

            while (banned[i] in wordList):
                del (wordList[wordList.index(banned[i])])

            i += 1

        occDict: dict = dict(Counter(wordList))
        maxOcc: int = max(occDict.values())

        for key in occDict:
            if occDict[key] == maxOcc:
                return key


paragraph = "a."
banned = []
obj = Solution()
solution = obj.mostCommonWord(paragraph, banned)
print(solution)
