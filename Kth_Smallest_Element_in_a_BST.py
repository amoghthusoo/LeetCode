# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def __init__(self):
        self.k = None
        self.count = 0
        self.out = None
    
    def traverse(self, root):
        
        if(root == None):
            return
        
        self.traverse(root.left)

        self.count += 1

        if(self.count == self.k):
            self.out = root.val
            return

        self.traverse(root.right)
        
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        self.k = k
        self.traverse(root)

        return self.out
