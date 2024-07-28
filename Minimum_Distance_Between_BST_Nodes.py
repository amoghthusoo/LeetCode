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


    def minDiffInBST(self, root: TreeNode) -> int:
        
        self.traverse(root)
        self.nums.sort()

        min_diff = int(2 ** 31)

        i = 1
        while(i < len(self.nums)):

            if((self.nums[i] - self.nums[i - 1]) < min_diff):
                min_diff = self.nums[i] - self.nums[i - 1]

            i += 1

        return min_diff