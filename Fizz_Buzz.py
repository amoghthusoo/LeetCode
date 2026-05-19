class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        
        ans = []
        for i in range(n):

            k = i + 1
            
            if(k % 15 == 0):
                ans.append("FizzBuzz")
            elif(k % 3 == 0):
                ans.append("Fizz")
            elif(k % 5 == 0):
                ans.append("Buzz")
            else:
                ans.append(str(k))
        
        return ans