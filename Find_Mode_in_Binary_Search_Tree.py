# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.occr_dict = {}
    
    def traverse(self, root):
        
        if(root == None):
            return
        
        self.traverse(root.left)

        if(root.val not in self.occr_dict):
            self.occr_dict[root.val] = 1
        else:
            self.occr_dict[root.val] += 1
            
        self.traverse(root.right)

    def findMode(self, root: TreeNode) -> list[int]:

        self.traverse(root)
        
        max_occr = -1

        for key, val in self.occr_dict.items():
            if(val > max_occr):
                max_occr = val

        out_arr = []

        for key, val in self.occr_dict.items():
            if(val == max_occr):
                out_arr.append(key)

        return out_arr