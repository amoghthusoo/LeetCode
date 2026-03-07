class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        
        ans = []
        start = 0
        current_ch = s[0]
        for i, e in enumerate(s):

            if(e != current_ch):
                
                if((i - start) >= 3):
                    ans.append([start, i - 1])
                
                start = i
                current_ch = e

        if((i - start + 1) >= 3):
            ans.append([start, i])
        
        return ans

s = "aaa"
obj = Solution()
result = obj.largeGroupPositions(s)
print(result)                