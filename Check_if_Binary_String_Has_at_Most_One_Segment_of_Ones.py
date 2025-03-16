class Solution:
    def checkOnesSegment(self, s: str) -> bool:

        one_mem = False

        last_index = None
        for index, ch in enumerate(s):

            if(ch == "0"):
                continue
            
            if(ch == "1" and not one_mem):
                last_index = index
                one_mem = True  
                continue

            if(ch == "1" and index - last_index == 1):
                last_index = index
            else:
                return False
    
        return True
    
s = "110"
obj = Solution()
out = obj.checkOnesSegment(s)
print(out)
