class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]

        i = 1
        while(i < len(dp)):
            
            j = 1
            while(j < len(dp[0])):

                if(text1[j - 1] == text2[i - 1]):
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

                j += 1
            i += 1
        
        return dp[-1][-1]
    
text1 = "abc"
text2 = "def" 
obj = Solution()
result = obj.longestCommonSubsequence(text1, text2)
print(result)