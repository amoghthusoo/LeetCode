# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.sum = 0
        self.ans = False
        self.traget = None

    def traverse(self, root):

        if(root == None or self.ans):
            return 
        
        self.sum += root.val
        self.traverse(root.left)
        self.traverse(root.right)

        if(root.left == root.right == None and self.sum == self.traget):
            self.ans = True
            return
        
        self.sum -= root.val


    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self.traget = targetSum
        self.traverse(root)
        return self.ans        