# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        
        if(root == None):
            return []

        bfs = []

        queue = [root]
        while(len(queue) != 0):
            
            level = []
            
            n = len(queue)
            for _ in range(n):

                node = queue.pop(0)
                level.append(node.val)
                
                if(node.left != None):
                    queue.append(node.left)
                
                if(node.right != None):
                    queue.append(node.right)
                
            bfs.append(level)

        return bfs

