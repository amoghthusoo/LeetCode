class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        
        i = 1
        while(i < len(s)):
            
            d1 = int(s[i - 1])
            d2 = int(s[i])

            if(abs(d1 - d2) > 2):
                return False
            
            i += 1
        
        return True