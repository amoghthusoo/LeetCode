# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.nums = []
    
    def traverse(self, root):
        
        if(root == None):
            return

        self.traverse(root.left)
        self.nums.append(root.val)
        self.traverse(root.right)

    def findTarget(self, root: TreeNode, k: int) -> bool:

        self.traverse(root)

        num_dict = {}

        num_dict[self.nums[0]] = None

        i = 1
        while(i < len(self.nums)):

            if((k - self.nums[i]) in num_dict):
                return True

            else:
                num_dict[self.nums[i]] = None

            i += 1

        return False