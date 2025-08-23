class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        
        out = []

        for q in queries:

            count = 0
            for p in points:

                if((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 <= q[2] ** 2):
                    count += 1
            
            out.append(count)

        return out

points = [[1,1],[2,2],[3,3],[4,4],[5,5]]
queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
obj = Solution()
out = obj.countPoints(points, queries)
print(out)       