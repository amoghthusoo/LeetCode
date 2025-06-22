class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        
        ans = []
        count = 0
        temp = ""
        for i in range(len(s)):
            
            temp += s[i]
            count += 1
            if(count == k):
                ans.append(temp)
                temp = ""
                count = 0
        
        if(len(temp) != 0):
            ans.append(temp)
            
            for _ in range(k - len(ans[-1])):
                ans[-1] += fill

        return ans
    
s = "abcdefghij"
k = 3
fill = "x"

obj = Solution()
result = obj.divideString(s, k, fill)
print(result)
