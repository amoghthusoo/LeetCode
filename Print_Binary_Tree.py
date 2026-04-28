# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.height = None
        self.res = None

    def get_height(self, root):

        if(root == None):
            return 0
        
        l = self.get_height(root.left)
        r = self.get_height(root.right)

        return 1 + max(l, r)
    
    def preorder(self, root, r, c):

        if(root == None):
            return
        
        self.res[r][c] = str(root.val)

        self.preorder(root.left, r + 1, c - 2 ** (self.height - r - 1))
        self.preorder(root.right, r + 1, c + 2 ** (self.height - r - 1))


    def printTree(self, root: TreeNode) -> list[list[str]]:
        
        self.height = self.get_height(root) - 1

        m = self.height + 1
        n = int(2 ** (self.height + 1)) - 1
        
        self.res = [["" for _ in range(n)] for _ in range(m)]

        self.preorder(root, 0, (n - 1)//2)

        return self.res

        

root = TreeNode(
    1,
    TreeNode(
        2,
        None,
        TreeNode(4)
    ),
    TreeNode(3)
)

obj = Solution()
result = obj.printTree(root)
print(result)