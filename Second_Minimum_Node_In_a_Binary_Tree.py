# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.set = set()

    def inorder(self, root):
        
        if(root == None):
            return 
        
        self.inorder(root.left)
        self.set.add(root.val)  
        self.inorder(root.right)

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        
        self.inorder(root)
        
        sorted_arr = sorted(list(self.set))


        try:
            return sorted_arr[1]
        except:
            return -1
