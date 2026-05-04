# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        
        self.inorder_traversal = []

    def inorder(self, root):

        if(root == None):
            return
        
        self.inorder(root.left)
        self.inorder_traversal.append(root.val)
        self.inorder(root.right)
    
    def isValidBST(self, root: TreeNode) -> bool:
        
        self.inorder(root)
        i = 1
        while(i < len(self.inorder_traversal)):
            
            if(self.inorder_traversal[i] <= self.inorder_traversal[i - 1]):
                return False

            i += 1

        return True
