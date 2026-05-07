# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def dfs(self, root):

        if(root == None):
            return 0

        queue = [root]
        depth = 0

        while(len(queue) != 0):

            n = len(queue)
            i = 0
            while(i < n):

                temp_node = queue.pop(0)

                if(temp_node.left != None):
                    queue.append(temp_node.left)
                
                if(temp_node.right != None):
                    queue.append(temp_node.right)

                i += 1
            
            depth += 1
        
        return depth

    def maxDepth(self, root: TreeNode) -> int:
        return self.dfs(root)