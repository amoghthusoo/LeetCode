# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def bfs(self, root):

        if(root == None):
            return 0

        queue = [root]
        depth = 0

        while(len(queue) != 0):

            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                
                if(node.left == None and node.right == None):
                    return depth + 1

                if(node.left != None):
                    queue.append(node.left)
                
                if(node.right != None):
                    queue.append(node.right)

            depth += 1

        
    def minDepth(self, root: TreeNode) -> int:
        
        return self.bfs(root)