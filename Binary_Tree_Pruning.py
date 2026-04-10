# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.contains_ones = False

    def check(self, root):
        
        if(self.contains_ones or root == None):
            return
        
        if(root.val == 1):
            self.contains_ones = True
            return

        self.check(root.left)
        self.check(root.right)

    def preorder(self, root):
        
        if(root == None):
            return
        
        if(root.left != None):
            self.contains_ones = False
            self.check(root.left)

            if(not self.contains_ones):
                root.left = None

        if(root.right != None):
            self.contains_ones = False
            self.check(root.right)

            if(not self.contains_ones):
                root.right = None


        self.preorder(root.left)
        self.preorder(root.right)

    def pruneTree(self, root: TreeNode) -> TreeNode:

        self.check(root)

        if(not self.contains_ones):
            return None
        
        self.preorder(root)
        return root