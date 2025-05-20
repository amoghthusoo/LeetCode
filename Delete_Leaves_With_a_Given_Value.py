# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def try_remove(self, root, target):
        try:
            if(root.left.val == target and root.left.left == None and root.left.right == None):
                root.left = None
        except:
            pass
        
        try:
            if(root.right.val == target and root.right.left == None and root.right.right == None):
                root.right = None
        except:
            pass

    def traverse(self, root, target):

        if(root == None):
            pass
        
        try:
            self.traverse(root.left, target)
        except:
            pass

        self.try_remove(root, target)
        
        try:
            self.traverse(root.right, target)
        except:
            pass
        
        self.try_remove(root, target)


    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        self.traverse(root, target)

        if(root.val == target and root.left == None and root.right == None):
            root = None

        return root