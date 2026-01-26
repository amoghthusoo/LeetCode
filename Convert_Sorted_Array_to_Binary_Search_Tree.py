# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        
        if(len(nums) == 0):
            return None
        
        mid_index = len(nums) // 2
        root_node = nums[mid_index]
        left_nums = nums[0 : mid_index]
        right_nums = nums[mid_index + 1 : ]

        root_node = TreeNode(root_node)
        root_node.left = self.sortedArrayToBST(left_nums)
        root_node.right = self.sortedArrayToBST(right_nums)

        return root_node
    





