class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        remainders = []
        columnNumber -= 1
        while(columnNumber >= 0):
            remainders.append(columnNumber % 26)
            columnNumber = columnNumber // 26
            columnNumber -= 1
        
        ans = ""
        i = -1
        while(i >= -len(remainders)):
            ans += chr(remainders[i] + 65)
            i -= 1
        
        return ans 
    
columnNumber = 701
obj = Solution()
result = obj.convertToTitle(columnNumber)
print(result)
