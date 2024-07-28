class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        
        node_dict = {i : 0 for i in range(1, len(edges) + 2)}
        
        for edge in edges:
            node_dict[edge[0]] += 1
            node_dict[edge[1]] += 1

        for key, val in node_dict.items():
            if(val == len(edges)):
                return key

edges = [[1,2],[5,1],[1,3],[1,4]]
obj = Solution()
out = obj.findCenter(edges)
print(out)