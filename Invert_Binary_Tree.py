# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.nodes = []

    def inorder(self, root):

        if(root == None):
            return
        
        self.inorder(root.left)
        self.nodes.append(root)    
        self.inorder(root.right)

    def invertTree(self, root: TreeNode) -> TreeNode:

        self.inorder(root)

        for node in self.nodes:
            node.left, node.right = node.right, node.left
                
        return root
    