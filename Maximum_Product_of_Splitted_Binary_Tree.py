# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def __init__(self):
        self.dict = dict()
        self.sum = 0
        self.total = 0
        self.ans = -1

    def get_sum(self, root):

        if(root == None):
            return 
        
        if(root in self.dict):
            self.sum += self.dict[root]
            return

        self.get_sum(root.left)
        self.sum += root.val 
        self.get_sum(root.right)
    
    def build_subtree_sum(self, root):
        
        if(root == None):
            return

        self.build_subtree_sum(root.left)
        self.build_subtree_sum(root.right)

        self.get_sum(root)
        self.dict[root] = self.sum
        self.sum = 0
    
    def traverse(self, root):

        if(root == None):
            return
        
        self.traverse(root.left)

        if(root.left != None):
            self.get_sum(root.left)
            temp = (self.total - self.sum) * self.sum 
            if(temp > self.ans):
                self.ans = temp 
            self.sum = 0

        if(root.right != None):
            self.get_sum(root.right)
            temp = (self.total - self.sum) * self.sum 
            if(temp > self.ans):
                self.ans = temp 
            self.sum = 0

        self.traverse(root.right)
        

    def maxProduct(self, root: TreeNode) -> int:
        
        self.build_subtree_sum(root)
        self.total = self.dict[root]
        self.traverse(root)

        return self.ans % (10 ** 9 + 7)
