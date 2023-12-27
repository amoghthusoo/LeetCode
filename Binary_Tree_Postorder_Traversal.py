# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.postorder_list = list()
    
    def postorder(self, root):

        if(root == None):
            return
        
        self.postorder(root.left)
        self.postorder(root.right)
        self.postorder_list.append(root.val)
        

    def postorderTraversal(self, root) -> list[int]:
        self.postorder(root)
        return self.postorder_list


root = TreeNode()
root.val = 10
root.left = TreeNode(5)
root.right = TreeNode(15)

obj = Solution()
out = obj.postorderTraversal(root)
print(out)        