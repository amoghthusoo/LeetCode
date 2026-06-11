class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        
        adj_list = dict()

        for edge in edges:
            u = edge[0]
            v = edge[1]

            if(u not in adj_list):
                adj_list[u] = [v]
            else:
                adj_list[u].append(v)

            if(v not in adj_list):
                adj_list[v] = [u]
            else:
                adj_list[v].append(u)
        

        level = 0
        visited = {1}
        queue = [1]
        while(queue):

            _len = len(queue)
            for _ in range(_len):
                node = queue.pop(0)
                for n in adj_list[node]:
                    if(n not in visited):
                        queue.append(n)
                        visited.add(n)

            level += 1
        
        depth = level - 1
        return pow(2, depth - 1, pow(10, 9) + 7)



edges = [[1,2]]
obj = Solution()
result = obj.assignEdgeWeights(edges)
print(result)
