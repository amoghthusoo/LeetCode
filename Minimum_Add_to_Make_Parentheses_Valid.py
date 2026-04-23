from collections import Counter
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        ans = 0
        stack = []
        for e in s:
            
            if(e == "("):
                stack.append("(")
            
            else:
                try:
                    stack.pop()
                except:
                    pass
        
        ans += len(stack)

        stack = []

        i = len(s) - 1
        while(i >= 0):
            
            if(s[i] == ")"):
                stack.append(")")
            
            else:
                try:
                    stack.pop()
                except:
                    pass

            i -= 1

        ans += len(stack)

        return ans