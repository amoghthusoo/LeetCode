class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        ans = 0
        while(numExchange <= numBottles):
            ans += numExchange
            numBottles += 1 - numExchange
            numExchange += 1
        return ans + numBottles
    
numBottles = 10
numExchange = 3
obj = Solution()
result = obj.maxBottlesDrunk(numBottles, numExchange)
print(result)
