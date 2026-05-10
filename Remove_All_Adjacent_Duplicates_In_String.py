class Solution:
    def removeDuplicates(self, s: str) -> str:

        s : list = list(s)

        i = 0
        while(i < len(s) - 1):

            if(s[i] == s[i + 1]):
                s.pop(i)
                s.pop(i)

                if(i != 0):
                    i -= 1
                
                continue

            i += 1

        out = ""
        for ch in s:
            out += ch
        return out
    
s = "aaaaaaaa"
obj = Solution()
out = obj.removeDuplicates(s)
print(out)