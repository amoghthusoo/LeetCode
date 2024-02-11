class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        
        points.sort()
        return max([points[i + 1][0] - points[i][0] for i in range(len(points) - 1)])

points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
obj = Solution()
out = obj.maxWidthOfVerticalArea(points)
print(out)