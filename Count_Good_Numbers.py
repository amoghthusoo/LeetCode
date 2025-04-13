class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        base = 20
        exponent = n // 2
        mod = (10 ** 9) + 7

        result = 1
        while(exponent > 0):
            
            if(exponent % 2 == 1):
                result = (result * base) % mod
            
            base = (base ** 2) % mod

            exponent >>= 1

        if(n % 2 == 0):
            return result
        
        else:
            return (result * 5) % mod
                    

# n = 806166225460393
n = 806166225460393
solution = Solution()
result = solution.countGoodNumbers(n)
print(result)
