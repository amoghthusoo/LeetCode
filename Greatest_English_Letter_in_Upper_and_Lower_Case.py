class Solution:
    def greatestLetter(self, s: str) -> str:
        
        visited = set(s)

        greastest = ""

        for ch in visited:

            if(ch.islower()):
                if(ch.upper() in visited):
                    if(ch.upper() > greastest):
                        greastest = ch.upper()
            
            else:
                if(ch.lower() in visited):
                    if(ch.upper() > greastest):
                        greastest = ch.upper()

        return greastest
                    
