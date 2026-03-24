# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.total = 0
    
    def inorder(self, root):
        
        if(root == None):
            return
        
        self.inorder(root.left)

        try:
            if(root.left.left == None and root.left.right == None):
                self.total += root.left.val
        except:
            pass

        self.inorder(root.right)
    
    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.inorder(root)
        return self.total
    