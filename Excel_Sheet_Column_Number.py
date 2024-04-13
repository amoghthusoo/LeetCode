class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        out = 0

        i = 0
        while(i < len(columnTitle)):
            
            out += (ord(columnTitle[i]) - 64) * int(26 ** (len(columnTitle) - 1 - i)) 
                        
            i += 1

        return out

columnTitle = "ZY"
obj = Solution()
out = obj.titleToNumber(columnTitle)
print(out)