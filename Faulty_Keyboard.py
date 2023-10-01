class Solution:
    def finalString(self, s: str) -> str:
        
        interList = []

        for ch in s:

            if (ch != 'i'):
                interList.append(ch)
            else:
                interList.reverse()

        outStr = ""

        for ch in interList:
            outStr += ch

        return outStr

s = "poiinter"
obj = Solution()
solution = obj.finalString(s)
print(solution)