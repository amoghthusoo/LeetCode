# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def contruct(self, preorder : list[int], postorder : list[int]):

        if(len(preorder) == len(postorder) == 0):
            return None
        
        elif((len(preorder) == len(postorder) == 1) and (preorder[0] == postorder[0])):
            temp = TreeNode(preorder[0])
            return temp
        
        root_element = preorder[0]

        left_subtree_root_element = preorder[1]
        left_subtree_root_element_index = postorder.index(left_subtree_root_element)
        
        left_subtree_postorder = postorder[0 : left_subtree_root_element_index + 1]
        right_subtree_postorder = postorder[left_subtree_root_element_index + 1 : len(postorder) - 1]
        
        left_subtree_preorder = preorder[1 : 1 + len(left_subtree_postorder)]
        right_subtree_preorder = preorder[1 + len(left_subtree_postorder) : ]

        temp = TreeNode()
        temp.val = root_element
        temp.left = self.contruct(left_subtree_preorder, left_subtree_postorder)
        temp.right = self.contruct(right_subtree_preorder, right_subtree_postorder)

        return temp
    
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode:
        return self.contruct(preorder, postorder)
    
preorder = [2,1]
postorder = [1,2]
solution = Solution()
result = solution.constructFromPrePost(preorder, postorder)
