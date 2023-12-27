# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.inorder_list = list()
    
    def inorder(self, root):

        if(root == None):
            return
        
        self.inorder(root.left)
        self.inorder_list.append(root.val)
        self.inorder(root.right)
        
        

    def inorderTraversal(self, root) -> list[int]:
        self.inorder(root)
        return self.inorder_list


root = TreeNode()
root.val = 10
root.left = TreeNode(5)
root.right = TreeNode(15)

obj = Solution()
out = obj.inorderTraversal(root)
print(out)        