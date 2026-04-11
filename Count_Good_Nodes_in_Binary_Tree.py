# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.stack = []
        self.count = 0

    def preorder(self, root):
        
        if(root == None):
            return
        
        try:
            max_element = max(self.stack)

            if(max_element <= root.val):
                self.count += 1

        except:
            self.count += 1

        self.stack.append(root.val) 

        self.preorder(root.left)
        self.preorder(root.right)

        self.stack.pop()

    def goodNodes(self, root: TreeNode) -> int:
        
        self.preorder(root)
        return self.count
    
root = TreeNode(
    3,
    TreeNode(
        1,
        TreeNode(3)
    ),
    TreeNode(
        4,
        TreeNode(1),
        TreeNode(5)
    )
)

obj = Solution()
result = obj.goodNodes(root)
print(result)
