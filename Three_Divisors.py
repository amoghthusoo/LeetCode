class Solution:
    def isThree(self, n: int) -> bool:
        
        divisor_count = 1

        i = 1
        while(i <= n // 2):

            if(n % i == 0):
                divisor_count += 1

            
            if(divisor_count > 3):
                return False

            i += 1

        if(divisor_count == 3):
            return True
        else:
            return False
    
n = 4
obj = Solution()
out = obj.isThree(n)
print(out)
    