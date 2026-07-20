# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        self.dp = dict()
        self.ans = 0

        def get_max(root):
            
            if(root in self.dp):
                return self.dp[root]

            if(root == None):
                return 0
            
            left_max = get_max(root.left)
            right_max = get_max(root.right)
            max_val = max(root.val, left_max, right_max)
            self.dp[root] = max_val
            return max_val

        def inorder(root):

            if(root == None):
                return
            
            inorder(root.left)
            inorder(root.right)
            max_val = get_max(root)
            if(root.val >= max_val):
                self.ans += 1


        inorder(root)
        return self.ans
