from collections import deque

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stack = deque()

        for token in tokens:

            if(token not in ["+", "-", "*", "/"]):
                stack.append(int(token))

            else:

                op2 = stack.pop()
                op1 = stack.pop()

                if(token == "+"):
                    r = op1 + op2

                elif(token == "-"):
                    r = op1 - op2

                elif(token == "*"):
                    r = op1 * op2

                else:
                    r = int(op1 / op2) 

                stack.append(r)

        return stack.pop()

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
obj = Solution()
result = obj.evalRPN(tokens)
print(result)       