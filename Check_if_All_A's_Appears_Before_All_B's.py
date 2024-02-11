class Solution:
    def checkString(self, s: str) -> bool:
        
        aMem = True
        i = 0
        while(i < len(s)):

            if(s[i] == 'b' and aMem):
                aMem = False
            
            elif(s[i] == 'a' and not aMem):
                return False
        
            i += 1

        return True
    
s = "bbb"
obj = Solution()
solution = obj.checkString(s)
print(solution)