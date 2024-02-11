class Solution:
    def sortSentence(self, s: str) -> str:
        
        s = s.split()
        interList = [None for i in range(len(s))]

        i = 0
        while (i < len(s)):
            
            interList[int(s[i][-1]) - 1] = s[i][0:-1] 
            i += 1

        outStr = ""

        i = 0
        while (i < len(interList)):
            
            outStr += interList[i]

            if (i != len(interList) - 1):
                outStr += " "
            
            i +=1 
        
        return outStr
        


s = "Myself2 Me1 I4 and3"
obj = Solution()
solution = obj.sortSentence(s)
print(solution)