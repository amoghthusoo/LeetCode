class Solution:
    def isBoomerang(self, points: list) -> bool:

        def slope(p1, p2) -> float | None:

            try:
                _slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
            except:
                _slope = None
            
            return _slope
        
        p1 = points[0]
        p2 = points[1]
        p3 = points[2]

        if  (
                (p1 == p2) or
                (p2 == p3) or
                (p1 == p3)
            ):
            return False
        
        else:
            
            slope1 = slope(p1, p2)
            slope2 = slope(p2, p3)

            if (slope1 != slope2):
                return True
            else:
                return False

points = [[0,0],[0,2],[2,1]]
obj = Solution()
solution = obj.isBoomerang(points)
print(solution)