# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.stack = []
        self.ans = 0

    def traverse(self, root):
        
        if(root is None):
            return
        
        self.stack.append(str(root.val))
        self.traverse(root.left)
        self.traverse(root.right)

        if(root.left == root.right == None):
            self.ans += int("".join(self.stack), 2)

        self.stack.pop()

    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.ans