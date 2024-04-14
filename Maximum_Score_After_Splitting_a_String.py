class Solution:
    def maxScore(self, s: str) -> int:
        
        maxScore = -1

        i = 0
        while(i < len(s) - 1):
            
            score = s[0 : i + 1].count("0") + s[i + 1 : ].count("1")
            if(score > maxScore):
                maxScore = score
            
            i += 1
        
        return maxScore

s = "1111"
obj = Solution()
out = obj.maxScore(s)
print(out)