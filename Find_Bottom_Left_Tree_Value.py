from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        levels = []
        queue = deque([root])

        while(queue):

            n = len(queue)
            level = []

            for _ in range(n):

                node = queue.popleft()
                level.append(node)

                if(node.left != None):
                    queue.append(node.left)
                
                if(node.right != None):
                    queue.append(node.right)
            
            levels.append(level)
        
        return levels[-1][0].val