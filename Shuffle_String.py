class Solution:
    def restoreString(self, s: str, indices: list) -> str:
        
        interList = [None for i in range(len(s))]
        outStr = ""

        i = 0
        while (i < len(s)):

            interList[indices[i]] = s[i]
            i += 1

        for letter in interList:
            outStr += letter

        return outStr
        

s = "abc"
indices = [0,1,2]
obj = Solution()
solution = obj.restoreString(s, indices)
print(solution)