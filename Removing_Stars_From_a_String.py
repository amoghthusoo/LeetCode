class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = []

        for e in s:
            if(e != "*"):
                stack.append(e)
            else:
                stack.pop()

        result = ""
        for e in stack:
            result += e
        
        return result
        
s = "leet**cod*e"
solution = Solution()
result = solution.removeStars(s)
print(result)