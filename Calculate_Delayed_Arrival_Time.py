class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        
        return (arrivalTime + delayedTime) % 24

arrivalTime = 13
delayedTime = 12
obj = Solution()
solution = obj.findDelayedArrivalTime(arrivalTime, delayedTime)
print(solution)