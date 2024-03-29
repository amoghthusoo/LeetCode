class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        n = str(n)
        result = 0

        sign = 1
        i = 0
        while(i < len(n)):
            
            result += int(n[i]) * sign
            sign *= -1

            i += 1

        return result

n = 886996
obj = Solution()
out = obj.alternateDigitSum(n)
print(out)