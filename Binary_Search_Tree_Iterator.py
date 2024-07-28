# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        
        self.node_list = []
        self.i = -1
        self.traverse(root)

    def traverse(self, root):

        if(root == None):
            return 
        
        self.traverse(root.left)
        self.node_list.append(root.val)
        self.traverse(root.right)

    def next(self) -> int:
        
        self.i += 1
        return self.node_list[self.i]

    def hasNext(self) -> bool:

        if(self.i + 1 < len(self.node_list)):
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()