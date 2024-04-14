class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        binStr = bin(n)[2:]

        i = 0
        while(i < len(binStr) - 1):
            
            if(binStr[i] == binStr[i + 1]):
                return False
            
            i += 1


        return True


n = 11
obj = Solution()
out = obj.hasAlternatingBits(n)
print(out)