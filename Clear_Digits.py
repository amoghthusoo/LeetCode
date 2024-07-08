class Solution:
    def clearDigits(self, s: str) -> str:
        
        s = list(s)

        i = 0
        while(i < len(s)):

            if(s[i].isdigit()):
                s.pop(i)
                s.pop(i - 1)
                i = 0
                continue

            i += 1

        out_str = ""
        for letter in s:
            out_str += letter

        return out_str
    
s = "abc"
obj = Solution()
out = obj.clearDigits(s)
print(out)