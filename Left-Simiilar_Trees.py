# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self):
        self.l1 = []
        self.l2 = []
        self.first_tree = True

    def traverse(self, root):

        if(root == None):
            return 
        
        if(root.left == root.right == None):

            if(self.first_tree):
                self.l1.append(root.val)
            else:
                self.l2.append(root.val)

        self.traverse(root.left)
        self.traverse(root.right)
    
    
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        self.traverse(root1)
        self.first_tree = False
        self.traverse(root2)

        if(self.l1 == self.l2):
            return True
        else:
            return False