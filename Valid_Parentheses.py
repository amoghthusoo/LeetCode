class Solution:
    def isValid(self, s: str) -> bool:
        
        def push(stack : list, element : str) -> None:
        
            stack.append(element)
            return None

        def pop(stack : list) -> str:
        
            if (len(stack) == 0):
                return None
            else:
                return stack.pop()
        
        def top(stack : list) -> None | str:
        
            if (isEmpty(stack)):
                return None
            else:
                return stack[-1]
            
        def isEmpty(stack : list) -> bool:
        
            if (len(stack) == 0):
                return True
            else:
                return False
        
        stack = []
        
        i = 0
        while (i < len(s)):

            if (isEmpty(stack)):
                push(stack, s[i])
            
            elif(   (s[i] == ')' and top(stack) == '(') or
                    (s[i] == '}' and top(stack) == '{') or
                    (s[i] == ']' and top(stack) == '[')
                ):
                pop(stack)
            
            else:
                push(stack, s[i])

            i += 1

        if isEmpty(stack):
            return True
        else:
            return False

s = "{[]}"
obj = Solution()
solution = obj.isValid(s)
print(solution)