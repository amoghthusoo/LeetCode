class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:

        adjacency_list = dict()

        for node in range(n):
            adjacency_list[node] = []

        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])        
            adjacency_list[edge[1]].append(edge[0])        

        # print(adjacency_list)

        visited = set()
        components = []
        for i in range(n):

            if(i not in visited):
                queue = [i]
            else:
                continue

            component = set()
            while(len(queue) != 0):

                n = len(queue)
                for _ in range(n):

                    active_node = queue.pop(0)
                    component.add(active_node)
                    visited.add(active_node)
                    
                    neighbours = []
                    for node in adjacency_list[active_node]:
                        if(node not in visited):
                            neighbours.append(node)

                    queue.extend(neighbours)

            components.append(component)

        count = 0
        for component in components:

            edges = set()
            for node in component:

                for neighbour in adjacency_list[node]:
                    
                    if((node, neighbour) not in edges and (neighbour, node) not in edges):
                        edges.add((node, neighbour))

            if(len(edges) == len(component) * (len(component) - 1) // 2):
                count += 1

        return count        
                
n = 6
edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
solution = Solution()
result = solution.countCompleteComponents(n, edges)
print(result)

