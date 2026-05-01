from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def __init__(self):
        self.dq = deque()
        self.ans = None
    
    def traverse(self, root):
        
        if(root == None):
            return 
        
        self.dq.appendleft(chr(root.val + 97))
        
        self.traverse(root.left)
        self.traverse(root.right)

        if(root.left == root.right == None):
            
            temp_str = "".join(self.dq)

            if(self.ans == None):
                self.ans = temp_str
            
            elif(temp_str < self.ans):
                self.ans = temp_str
        
        self.dq.popleft()


    def smallestFromLeaf(self, root: TreeNode) -> str:
        
        self.traverse(root)
        return self.ans