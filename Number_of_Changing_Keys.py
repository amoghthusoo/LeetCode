class Solution:
    def countKeyChanges(self, s: str) -> int:
        
        if(len(s) == 1):
            return 0
        

        count = 0
        i = 0
        while(i < len(s) - 1):

            if( (s[i] == s[i + 1]) or
                (s[i].islower() and s[i + 1] == s[i].upper()) or
                (s[i].isupper() and s[i + 1] == s[i].lower())
               ):
                pass

            else:
                count += 1

            i += 1

        return count