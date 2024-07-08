class Solution:
    def checkRecord(self, s: str) -> bool:
        
        if(s.count("A") >= 2):
            return False
        

        i = 0
        while(i < len(s) - 2):

            if(s[i] == s[i + 1] == s[i + 2] == "L"):
                return False
            i += 1

        return True

