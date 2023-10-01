class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        s = s.split()
        outStr = ""

        for i in range(k):
            outStr += s[i]

            if (i != k - 1):
                outStr += " "
        
        return outStr

s = "chopper is not a tanuki"
k = 5
obj = Solution()
solution = obj.truncateSentence(s, k)
print(solution)