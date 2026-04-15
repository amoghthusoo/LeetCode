class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        
        U = set([i for i in range(n)])
        in_deg_vertices = set()

        for edge in edges:
            in_deg_vertices.add(edge[1])
        
        diff = U.difference(in_deg_vertices)

        if(len(diff) == 1):
            return next(iter(diff))
        else:
            return -1
        
n = 4
edges = [[0,2],[1,3],[1,2]]
obj = Solution()
result = obj.findChampion(n, edges)
print(result)