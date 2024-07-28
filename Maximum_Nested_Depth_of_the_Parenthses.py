class Solution:
    def maxDepth(self, s: str) -> int:

        stack = []
        max_depth = 0

        for e in s:

            if(e == '('):
                stack.append('(')

                if(len(stack) > max_depth):
                    max_depth = len(stack)

            elif(e == ')'):
                stack.pop()


        return max_depth