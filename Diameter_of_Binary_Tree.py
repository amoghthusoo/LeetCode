# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0
        self.heights = {None : 0}

    def get_height(self, root):

        if(root in self.heights):
            return self.heights[root]

        if(root == None):
            self.heights[root] = 0
            return 0
    
        elif(root.left == None and root.right == None):
            return 0
        
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        self.heights[root.left] = left
        self.heights[root.right] = right
        
        return 1 + max(left, right)
    

    def traverse(self, root):

        if(root == None):
            return

        left_path, right_path = 0, 0    
        if(root.left != None):
            left_path = 1 + self.get_height(root.left)
        
        if(root.right != None):
            right_path = 1 + self.get_height(root.right)
        
        _sum = left_path + right_path
        if(_sum > self.ans):
            self.ans = _sum

        self.traverse(root.left)
        self.traverse(root.right)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.traverse(root)
        return self.ans
        