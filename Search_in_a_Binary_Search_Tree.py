# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def __init__(self):
        self.val = None
        self.result = None

    def search(self, root):
        
        if(root == None):
            return
        
        if(root.val == self.val):
            self.result = root
            return
        
        elif(root.val < self.val):
            self.search(root.right)

        else:
            self.search(root.left)


    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        self.val = val
        self.search(root)

        return self.result