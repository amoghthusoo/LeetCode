class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        MOD = int(10 ** 9) + 7
        ans = 0

        i = 1
        while(i <= n):

            bin_str = bin(i)[2 : ]
            for b in bin_str:
                if(b == "0"):
                    ans = ans * 2
                else:
                    ans = (ans * 2) + 1
                
                ans = ans % MOD

            i += 1
        
        return ans

n = 12
obj = Solution()
result = obj.concatenatedBinary(n)
print(result)