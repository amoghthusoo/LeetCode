# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.occr_dict = dict()

    def inorder(self, root):
        
        if(root == None):
            return

        self.inorder(root.left)

        if(root.val not in self.occr_dict):
            self.occr_dict[root.val] = 1
        else:
            self.occr_dict[root.val] += 1

        self.inorder(root.right)

    def isUnivalTree(self, root: TreeNode) -> bool:
        
        self.inorder(root)
        keys = self.occr_dict.keys()

        if(len(keys) == 1):
            return True
        else:
            return False