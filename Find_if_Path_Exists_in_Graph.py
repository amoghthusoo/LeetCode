from collections import deque

class Solution:

    def __init__(self):
        self.visited = set()
        self.adj_list = dict()

    def construct_adj_list(self, n, edges):
        
        for i in range(n):
            self.adj_list[i] = set()

        for edge in edges:

            i = edge[0]
            j = edge[1]
            
            self.adj_list[i].add(j)
            self.adj_list[j].add(i)

    def bfs(self, s, d):
        
        queue = deque([s])

        while(queue):

            node = queue.popleft()

            if(node == d):
                return True
            
            self.visited.add(node)

            for e in self.adj_list[node]:

                if(e not in self.visited):
                    self.visited.add(e)
                    queue.append(e)
                    
        return False


    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        
        self.construct_adj_list(n, edges)
        return self.bfs(source, destination)
    
n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5
obj = Solution()
result = obj.validPath(n, edges, source, destination)
print(result)