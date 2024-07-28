# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.total = 0
        self.low = None
        self.high = None

    def traverse(self, root):

        if(root == None):
            return

        self.traverse(root.left)

        if(root.val >= self.low and root.val <= self.high):
            self.total += root.val
        
        self.traverse(root.right)
    
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        self.low = low
        self.high = high

        self.traverse(root)

        return self.total