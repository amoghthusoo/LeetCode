# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.out_root = None
        self.tree_end = None

    def insert(self, val):

        temp = TreeNode(val)
        
        if(self.out_root == None):
            self.out_root = temp
            self.tree_end = temp
            return
        
        self.tree_end.right = temp
        self.tree_end = temp
        
    def traverse(self, root):
        
        if(root == None):
            return 
        
        self.traverse(root.left)
        self.insert(root.val)
        self.traverse(root.right)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        self.traverse(root)
        return self.out_root