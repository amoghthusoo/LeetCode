# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def __init__(self):
        self.is_balanced = True
    
    def get_height(self, root):
        
        if(root == None): 
            return -1
        
        elif(root.left == None and root.right == None):
            return 0
        
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def preorder(self, root):
            
            if(root == None):
                return
            
            h1 = 1 + self.get_height(root.left)
            h2 = 1 + self.get_height(root.right)

            if(self.is_balanced and abs(h1 - h2) > 1):
                self.is_balanced = False
            
            self.preorder(root.left)
            self.preorder(root.right)

    def isBalanced(self, root: TreeNode) -> bool:

        self.preorder(root)
        return self.is_balanced

root = TreeNode(1,
                None,
                TreeNode(
                    2, 
                    None,
                    TreeNode(3)                    
                )
)
obj = Solution()
result = obj.isBalanced(root)
print(result)