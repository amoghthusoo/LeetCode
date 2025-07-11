# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        
        if(len(preorder) == 0):
            return None
        
        root_val = preorder.pop(0)
        root_index = inorder.index(root_val)

        left_inorder = inorder[0 : root_index]
        right_inorder = inorder[root_index + 1 : ]

        left_preorder = preorder[0 : len(left_inorder)]
        right_preorder = preorder[len(left_inorder) : ]

        root_node = TreeNode(root_val)
        root_node.left = self.buildTree(left_preorder, left_inorder)
        root_node.right = self.buildTree(right_preorder, right_inorder)

        return root_node
    
