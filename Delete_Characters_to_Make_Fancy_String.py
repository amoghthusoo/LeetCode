class Solution:
    def makeFancyString(self, s: str) -> str:
        
        final_str = ""

        final_str += s[0:2]

        i = 2
        while(i < len(s)):

            if(s[i] == s[i - 1] == s[i - 2]):
                pass
            else:
                final_str += s[i]

            i += 1
        
        return final_str
        
s = "aab"
obj = Solution()
out = obj.makeFancyString(s)
print(out)