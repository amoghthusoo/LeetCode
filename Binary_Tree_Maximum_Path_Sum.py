# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.ans = float("-inf")

        def solve(root):

            if(root == None):
                return 0

            left_sum = solve(root.left)
            if(left_sum < 0):
                left_sum = 0

            right_sum = solve(root.right)
            if(right_sum < 0):
                right_sum = 0

            self.ans = max(self.ans, left_sum + root.val + right_sum)

            return root.val + max(left_sum, right_sum)

        solve(root)
        return self.ans