# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:

    def __init__(self):
        self.adj_list = dict()

    def construct_adj_list(self, node):
        
        if(node.val not in self.adj_list):
            self.adj_list[node.val] = []

            for n in node.neighbors:
                self.adj_list[node.val].append(n.val)

            for n in node.neighbors:
                self.construct_adj_list(n)

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if(node == None):
            return None
        
        self.construct_adj_list(node)

        nodes = []
        for i in range(1, len(self.adj_list) + 1):
            temp = Node()
            temp.val = i
            nodes.append(temp)

        for n in nodes:

            neighbor_vals = self.adj_list[n.val]
            for val in neighbor_vals:
                n.neighbors.append(nodes[val - 1])
        
        return nodes[0]