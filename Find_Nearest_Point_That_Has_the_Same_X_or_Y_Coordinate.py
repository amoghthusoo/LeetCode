class Solution:
    
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        
        outIndex = -1
        minDistance = 2 ** 31 - 1

        for index, point in enumerate(points): 
            
            if(point[0] == x or point[1] == y):
                
                tempDistance = abs(x - point[0]) + abs(y - point[1])
                if (tempDistance < minDistance):
                    minDistance = tempDistance
                    outIndex = index

        return outIndex


x = 3
y = 4
points = [[2, 3]]
obj = Solution()
out = obj.nearestValidPoint(x, y, points)
print(out)