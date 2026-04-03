class Solution:
    def findSmallestSetOfVertices(self, n, edges):

        return list(set(range(n)).difference({edge[1] for edge in edges})) 

n = 5
edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
solution = Solution()
result = solution.findSmallestSetOfVertices(n, edges)
print(result)