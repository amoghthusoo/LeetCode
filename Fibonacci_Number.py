class Solution:
    def fib(self, n: int) -> int:
        
        if (n == 0):
            return 0
        elif (n == 1):
            return 1
        else:
            firstNum = 0
            secondNum = 1
            
            i = 2
            while(i <= n):
                
                resultNum = firstNum + secondNum
                firstNum = secondNum
                secondNum = resultNum
                
                i += 1
            
            return resultNum
                

n = 4
obj = Solution()
solution = obj.fib(n)
print(solution)