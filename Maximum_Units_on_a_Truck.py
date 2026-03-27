class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:

        boxTypes = sorted(boxTypes, key = lambda x : x[1], reverse=True)

        max_units = 0
        capacity = 0

        for boxType in boxTypes:
            
            if(capacity + boxType[0] <= truckSize):
                max_units += boxType[0] * boxType[1]
                capacity += boxType[0]
            else:
                max_units += (truckSize - capacity) * boxType[1]
                capacity = truckSize

        return max_units
    
boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
obj = Solution()
out = obj.maximumUnits(boxTypes, truckSize)
print(out)