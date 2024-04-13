class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        letterList = []
        symbolDict = {}

        i = 0
        while(i < len(s)):

            if(ord(s[i]) in range(65, 91) or ord(s[i]) in range(97,123)):
                letterList.append(s[i])
            else:
                symbolDict[i] = s[i]

            i += 1


        outString = ""
        for i in range(len(s)):

            if(i in symbolDict):
                outString += symbolDict[i]
            else:
                outString += letterList.pop()

        return outString


       



s = "Test1ng-Leet=code-Q!"
obj = Solution()
out = obj.reverseOnlyLetters(s)
print(out)