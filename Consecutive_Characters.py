from collections import Counter
class Solution:
    def maxPower(self, s: str) -> int:
        
        stack = []
        consecutiveOccList = []

        i = 0
        while (i < len(s)):

            if (len(stack) == 0):
                stack.append(s[i])
            
            elif (s[i] != stack[-1]):
                count = 0
                while (len(stack) != 0):
                    stack.pop()
                    count += 1
                consecutiveOccList.append(count)
                stack.append(s[i])
            
            elif (s[i] == stack[-1]):
                stack.append(s[i])

            i += 1
        
        if (len(stack) > 0):
            count = 0
            while (len(stack) != 0):
                stack.pop()
                count += 1
            consecutiveOccList.append(count)
        
        
        return max(consecutiveOccList)
        

s = "cc"
obj = Solution()
solution = obj.maxPower(s)
print(solution)