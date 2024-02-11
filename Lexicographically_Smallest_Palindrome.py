class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        
        ordList = [ord(ch) for ch in s]
        
        i = 0
        j = len(ordList) - 1

        while (i < j):

            if (ordList[i] < ordList[j]):
                ordList[j] = ordList[i]
            elif (ordList[i] > ordList[j]):
                ordList[i] = ordList[j]

            i += 1
            j -= 1

        interList = [chr(i) for i in ordList]
        outStr = ""

        for ch in interList:
            outStr += ch

        return outStr

s = "seven"
obj = Solution()
solution = obj.makeSmallestPalindrome(s)
print(solution)