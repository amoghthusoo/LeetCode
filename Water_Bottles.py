class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        extras = 0

        numBottles_temp = numBottles
        while(numBottles_temp >= numExchange):


            extras += numBottles_temp // numExchange
            numBottles_temp = (numBottles_temp // numExchange) + (numBottles_temp % numExchange)

        return numBottles + extras
    
numBottles = 15
numExchange = 4
obj = Solution()
out = obj.numWaterBottles(numBottles, numExchange)
print(out)
