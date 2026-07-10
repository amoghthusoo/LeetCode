from collections import deque

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:

        def bfs(src, adj_list):

            visited = {src}
            queue = deque([src])
            component = set()
            while(queue):

                popped = queue.popleft()
                component.add(popped)

                for child in adj_list[popped]:

                    if(child not in visited):
                        queue.append(child)
                        visited.add(child)
            
            return component
        
        adj_list = dict()
        for i in range(1, n + 1):
            adj_list[i] = set()

        for road in roads:
            src = road[0]
            dest = road[1]

            adj_list[src].add(dest)
            adj_list[dest].add(src)
        
        target_comp = bfs(1, adj_list)
        
        _min = float("inf")
        for road in roads:
            src = road[0]
            dest = road[1]
            cost = road[2]

            if(src in target_comp and dest in target_comp):
                _min = min(_min, cost)

        return _min
    
n = 4
roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
obj = Solution()
result = obj.minScore(n, roads)
print(result)