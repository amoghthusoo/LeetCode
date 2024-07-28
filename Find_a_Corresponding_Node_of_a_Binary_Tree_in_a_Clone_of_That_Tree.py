# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.out_node = None
        self.target_val = None

    def traversal(self, root):
        
        if(root == None):
            return
        
        self.traversal(root.left)

        if(root.val == self.target_val):
            self.out_node = root
            return 
        
        self.traversal(root.right)

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        self.target_val = target.val
        self.traversal(cloned)

        return self.out_node
