# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.preorder_list = []

    def preorder(self, root):
        if(root == None):
            return
        
        self.preorder_list.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def insert(self, head, rear, val):

        if(head == rear == None):
            temp = TreeNode()
            temp.val = val
            head = rear = temp

        else:
            temp = TreeNode()
            temp.val = val
            rear.right = temp
            rear = temp

        return head, rear


    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if(root == None):
            return

        self.preorder(root)
        
        head = rear = None

        for val in self.preorder_list:
            head, rear = self.insert(head, rear, val)

        root.left = None
        root.right = head.right

        