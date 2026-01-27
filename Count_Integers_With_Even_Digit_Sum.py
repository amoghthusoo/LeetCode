class Solution:
    def countEven(self, num: int) -> int:
        
        def digit_sum(n):

            n = str(n)

            total = 0
            for d in n:
                total += int(d)
            
            return total

        ans = 0
        for i in range(1, num + 1):

            if(digit_sum(i) % 2 == 0):
                ans += 1
        
        return ans