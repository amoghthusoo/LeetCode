from copy import deepcopy
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
        self.ans = []
        self.traget = None

    def traverse(self, root):
        
        if(root == None):
            return 
        
        self.stack.append(root.val)
        self.sum += root.val

        self.traverse(root.left)
        self.traverse(root.right)


        if(root.left == root.right == None and self.sum == self.traget):
            self.ans.append(deepcopy(self.stack))

        self.stack.pop()
        self.sum -= root.val


    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        
        self.traget = targetSum
        self.traverse(root)
        return self.ans