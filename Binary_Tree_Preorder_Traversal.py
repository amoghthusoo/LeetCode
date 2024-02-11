# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.preorder_list = list()
    
    def preorder(self, root):

        if(root == None):
            return
        
        self.preorder_list.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
        

    def preorderTraversal(self, root) -> list[int]:
        self.preorder(root)
        return self.preorder_list


root = TreeNode()
root.val = 10
root.left = TreeNode(5)
root.right = TreeNode(15)

obj = Solution()
out = obj.preorderTraversal(root)
print(out)        