# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.min = None
        self.max = None
        self.max_diff = -1

    def update_min_max(self, root):
        
        if(root == None):
            return
        
        self.update_min_max(root.left)

        if(root.val < self.min):
            self.min = root.val

        if(root.val > self.max):
            self.max = root.val

        self.update_min_max(root.right)

    def traverse(self, root):

        if(root == None):
            return
        
        self.traverse(root.left)

        self.min = int(10 ** 5 + 1)
        self.max = -1

        self.update_min_max(root)

        temp_val = max(abs(root.val - self.min), abs(root.val - self.max))
        if(temp_val > self.max_diff):
            self.max_diff = temp_val

        self.traverse(root.right)

    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        self.traverse(root)
        return self.max_diff
