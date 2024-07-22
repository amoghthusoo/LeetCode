class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        s = list(s)
        stack = []

        i = 0
        while(i < len(s)):

            if(s[i] == "("):
                stack.append(i)
            
            elif(s[i] == ")"):

                start = stack.pop()
                end = i - 1
                reversed_str = s[end : start : -1]

                x = start + 1
                for letter in reversed_str:
                    s[x] = letter

                    x += 1

            i += 1

        out_str = ""

        for letter in s:
            
            if(letter not in ["(", ")"]):
                out_str += letter

        return out_str

s = "(ed(et(oc))el)"
obj = Solution()
out = obj.reverseParentheses(s)
print(out)