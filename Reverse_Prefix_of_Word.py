class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        interList = []
        firstOccMem = False
        for letter in word:

            if (letter != ch):
                interList.append(letter)
            else:
                interList.append(letter)
                if (not firstOccMem):
                    interList.reverse()
                    firstOccMem = True

        outStr = ""

        for element in interList:
            outStr += element

        return outStr


word = "abcd"
ch = "z"
obj = Solution()
solution = obj.reversePrefix(word, ch) 
print(solution)