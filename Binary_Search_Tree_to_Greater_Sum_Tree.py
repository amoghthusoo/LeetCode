# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.node_vals = []
        self.sum_dict = {}

    def traverse(self, root):

        if(root == None):
            return

        self.traverse(root.left)
        self.node_vals.append(root.val)
        self.traverse(root.right)

    def modify(self, root):
        
        if(root == None):
            return

        self.modify(root.left)
        root.val += self.sum_dict[root.val]
        self.modify(root.right)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        self.traverse(root)
        self.node_vals.sort()

        total = 0
        i = len(self.node_vals) - 1
        while(i >= 0):

            self.sum_dict[self.node_vals[i]] = total
            total += self.node_vals[i]

            i -= 1
        
        self.modify(root)

        return root
