class Solution:
    def processStr(self, s: str) -> str:
        
        arr = []

        for e in s:
            
            if(e == "*"):
                try:
                    arr.pop()
                except:
                    pass
            elif(e == "#"):
                arr *= 2
            elif(e == "%"):
                arr.reverse()
            else:
                arr.append(e)
        
        return "".join(arr)