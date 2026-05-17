# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.stack = []

    def traverse(self, root):

        if(root == None):
            return 

        self.traverse(root.left)
        self.traverse(root.right)

        if(root.val not in {2, 3}):
            self.stack.append(root.val)
        else:
            o2 = self.stack.pop()
            o1 = self.stack.pop()
            
            if(root.val == 2):    
                r = o1 or o2
            else:
                r = o1 and o2
                
            self.stack.append(r)
        

    def evaluateTree(self, root: TreeNode) -> bool:
        
        self.traverse(root)
        return bool(self.stack.pop())