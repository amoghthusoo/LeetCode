from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = None, children = None):
        self.val = val
        self.children = children


class Solution:

    def bfs(self, root):

        if(root == None):
            return 0

        queue = deque([root])
        depth = 0
        while(queue):

            n = len(queue)
            for _ in range(n):

                popped = queue.popleft()

                for child in popped.children:
                    queue.append(child)
            
            depth += 1
        
        return depth

    def maxDepth(self, root) -> int:
        
        depth = self.bfs(root)
        return depth