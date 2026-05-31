class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        
        c_indices = []
        for i, ch in enumerate(s):
            if(ch == c):
                c_indices.append(i)
        
        ans = []

        x = 0
        i = 0
        while(i < len(c_indices)):

            while(x <= c_indices[i]):

                ans.append(min(abs(c_indices[i] - x), abs(c_indices[i - 1] - x)))
                x += 1

            i += 1

        while(x < len(s)):
            ans.append(abs(c_indices[-1] - x))
            x += 1

        return ans

s = "loveleetcode"
c = "e"
obj = Solution()
result = obj.shortestToChar(s, c)
print(result)