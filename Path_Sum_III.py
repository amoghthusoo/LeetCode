# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.sum = 0
        self.target = None
        self.count = 0

    def detect_sum(self, root):
        
        if(root == None):
            return 
        
        self.sum += root.val

        self.detect_sum(root.left)
        self.detect_sum(root.right)

        if(self.sum == self.target):
            self.count += 1

        self.sum -= root.val

    
    def preorder(self, root):

        if(root == None):
            return

        self.sum = 0
        self.detect_sum(root)

        self.preorder(root.left)
        self.preorder(root.right)

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        
        self.target = targetSum
        self.preorder(root)
        
        return self.count