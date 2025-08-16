from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = None, children = None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> list[list[int]]:

        if(root == None):
            return []
        
        levels = []
        queue = deque([root])

        while(queue):

            level = []
            n = len(queue)
            for _ in range(n):

                node = queue.popleft()
                level.append(node.val)

                for child in node.children:
                    queue.append(child)

            levels.append(level)

        return levels                