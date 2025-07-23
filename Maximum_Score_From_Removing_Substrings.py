class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        stack = []
        score = 0

        if(x >= y):
            first_ch = "a"
            second_ch = "b"
        else:
            first_ch = "b"
            second_ch = "a"

        for ch in s:

            if(not stack):
                stack.append(ch)
            
            else:

                if(ch == second_ch and stack[-1] == first_ch):
                    stack.pop()
                    if(x >= y):
                        score += x
                    else:
                        score += y
                
                else:
                    stack.append(ch)

        intr_str = "".join(stack)
        stack = []
    
        for ch in intr_str:

            if(not stack):
                stack.append(ch)
            
            else:

                if(ch == first_ch and stack[-1] == second_ch):
                    stack.pop()
                    if(x >= y):
                        score += y
                    else:
                        score += x
                else:
                    stack.append(ch)

        return score

s = "cdbcbbaaabab"
x = 4
y = 5
obj = Solution()
result = obj.maximumGain(s, x, y)
print(result)