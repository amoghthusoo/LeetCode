# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.stack = []
        self.ans = []

    def traverse(self, root):

        if(root == None):
            return
        
        self.stack.append(str(root.val))

        self.traverse(root.left)
        self.traverse(root.right)   

        if(root.left == root.right == None):
            self.ans.append("->".join(self.stack))

        self.stack.pop()

        

    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        
        self.traverse(root)
        return self.ans
