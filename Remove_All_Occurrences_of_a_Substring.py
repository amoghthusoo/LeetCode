class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        while(part in s):
            i = s.find(part)
            s = s[0:i] + s[i + len(part) : ]
        
        return s
    
s = "aabababa"
part = "aba"
obj = Solution()
out = obj.removeOccurrences(s, part)
print(out)
