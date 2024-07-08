class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        if(len(s) == 1 and s[0] == "1"):
            return True
      
        
        elif(len(s) == 2):
            if(s[0] == "1" or s[1] == "1"):
                return True
        
        else:
            i = 1
            while(i < len(s)):
                if(s[i] == s[i - 1] == '1'):
                    return True
                
                i += 1

            return False
        
        return False