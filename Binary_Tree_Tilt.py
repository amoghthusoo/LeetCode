# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.subtreeSum = {None : 0}
        self.ans = 0
    
    def getSum(self, root):

        if(root in self.subtreeSum):
            return self.subtreeSum[root]

        if(root == None):
            return 0
        
        leftSum = self.getSum(root.left)
        self.subtreeSum[root.left] = leftSum

        rightSum = self.getSum(root.right)
        self.subtreeSum[root.right] = rightSum

        return leftSum + rightSum + root.val
    

    def traverse(self, root):

        if(root == None):
            return

        self.traverse(root.left)
        self.traverse(root.right)
        self.ans += abs(self.subtreeSum[root.left] - self.subtreeSum[root.right])

    def findTilt(self, root: TreeNode) -> int:
        
        self.getSum(root)
        self.traverse(root)
        return self.ans