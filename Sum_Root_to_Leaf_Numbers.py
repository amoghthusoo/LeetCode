# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.stack = []
        self.sum = 0

    def preorder(self, root):
        
        if(root == None):
            return 

        self.stack.append(str(root.val))

        self.preorder(root.left)
        self.preorder(root.right)

        if(root.left == root.right == None):

            num_str = "".join(self.stack)
            self.sum += int(num_str)

        self.stack.pop()


    def sumNumbers(self, root: TreeNode) -> int:
        
        self.preorder(root)
        return self.sum