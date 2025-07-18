# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:

        if(len(inorder) == 0):
            return None
        
        root_val = postorder.pop()
        root_index = inorder.index(root_val)

        left_inorder = inorder[0 : root_index]
        right_inorder = inorder[root_index + 1 : ]

        left_postorder = postorder[0 : len(left_inorder)]
        right_postorder = postorder[len(left_inorder) : ]

        root_node = TreeNode(root_val)
        root_node.left = self.buildTree(left_inorder, left_postorder)
        root_node.right = self.buildTree(right_inorder, right_postorder)

        return root_node