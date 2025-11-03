from collections import deque
class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        
        intr_arr = zip(colors, neededTime)
        
        stack = deque()

        ans = 0
        for e in intr_arr:

            if(not stack):
                stack.append(e)
            else:

                if(stack[-1][0] != e[0]):
                    stack.append(e)
                
                else:

                    if(e[1] < stack[-1][1]):
                        ans += e[1]
                    
                    else:
                        popped = stack.pop()
                        stack.append(e)
                        ans += popped[1]
        
        return ans



colors = "aabaa"
neededTime = [1,2,3,4,1]
obj = Solution()
result = obj.minCost(colors, neededTime)
print(result)