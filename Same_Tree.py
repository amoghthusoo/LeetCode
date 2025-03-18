# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.tree1 = []
        self.tree2 = []

    def inorder_t(self, root, arr):

        if(root == None):
            return

        self.inorder_t(root.left, arr)

        temp = []
        temp.append(root.val)
        try:
            temp.append(root.left.val)
        except:
            temp.append(None)
        try:
            temp.append(root.right.val)
        except:
            temp.append(None)
        
        arr.append(temp)
        self.inorder_t(root.right, arr)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        self.inorder_t(p, self.tree1)
        self.inorder_t(q, self.tree2)

        if(self.tree1 == self.tree2):
            return True

        else:
            return False