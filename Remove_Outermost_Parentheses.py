class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        ans = ""
        temp = ""
        c = 0
        for ch in s:

            temp += ch

            if(ch == "("):
                c += 1
            else:
                c -= 1

            if(c == 0):
                ans += temp[1 : len(temp) - 1] 
                temp = ""

        return ans

s = "()()"
obj = Solution()
result = obj.removeOuterParentheses(s)
print(result)           
