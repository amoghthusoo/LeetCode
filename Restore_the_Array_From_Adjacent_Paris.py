from collections import deque

class Solution:

    def __init__(self):
        self.al = dict()
        self.ans = []

    def construct_al(self, edges) -> None:

        for edge in edges:
            u, v = edge[0], edge[1]

            if(u not in self.al):
                self.al[u] = {v}
            else:
                self.al[u].add(v)
            
            if(v not in self.al):
                self.al[v] = {u}
            else:
                self.al[v].add(u)
    
    def find_zero_degree_vertex(self) -> int:

        for v, s in self.al.items():
            if(len(s) == 1):
                return v
            
    def bfs(self, s) -> None:

        queue = deque([s])
        visited = {s}

        while(len(queue) != 0):

            popped = queue.popleft()
            self.ans.append(popped)

            for v in self.al[popped]:

                if(v not in visited):
                    visited.add(v)
                    queue.append(v)

        
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        
        self.construct_al(adjacentPairs)
        s = self.find_zero_degree_vertex()
        self.bfs(s)
        return self.ans

adjacentPairs = [[2,1],[3,4],[3,2]]
obj = Solution()
result = obj.restoreArray(adjacentPairs)
print(result)

        