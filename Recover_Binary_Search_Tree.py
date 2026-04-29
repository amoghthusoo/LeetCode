# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self):
        self.nodes = []
        self.vals = []

    def inorder(self, root):

        if(root == None):
            return
        

        self.inorder(root.left)
        self.nodes.append(root)
        self.vals.append(root.val)
        self.inorder(root.right)
        

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder(root)

        self.vals.sort()

        i = 0
        while(i < len(self.nodes)):
            
            self.nodes[i].val = self.vals[i]
            i += 1

        