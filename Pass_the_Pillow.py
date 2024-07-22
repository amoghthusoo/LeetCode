class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        x = (2 * n) - 2

        if(time < x):

            if(time < n):
                return time + 1

            else:
                return x - time + 1

        else:

            y = time % x
            
            if(y < n):
                return y + 1
            else:
                return x - y + 1