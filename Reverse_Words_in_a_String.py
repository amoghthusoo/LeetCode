class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split()
        s.reverse()
        
        outStrList = []

        for word in s:
            outStrList.append(word)
            outStrList.append(" ")
                
        outStrList.pop()
        
        outStr = ""

        for word in outStrList:
            outStr += word
        
        return outStr        

s = "a good   example"
obj = Solution()
solution = obj.reverseWords(s)
print(solution)


