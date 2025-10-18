class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        i = 0
        j = 0

        while(i < len(t)):

            while(j < len(s) and s[j] != t[i]):
                j += 1
            
            if(j == len(s)):
                break

            j += 1
            i += 1

        return len(t) - i

s = "z"
t = "abcde"
obj = Solution()
result = obj.appendCharacters(s, t)
print(result)
