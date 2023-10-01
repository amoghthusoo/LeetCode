class Solution:
    def isAcronym(self, words: list, s: str) -> bool:
        
        checkStr = ""

        for element in words:
            checkStr += element[0]

        if (checkStr == s):
            return True
        else:
            return False


words = ["never","gonna","give","up","on","you"]
s = "ngguoy"
obj = Solution()
solution = obj.isAcronym(words, s)
print(solution)