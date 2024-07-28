# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.node_vals_1 = []
        self.node_vals_2 = []

    def traverse_1(self, root):

        if(root == None):
            return

        self.traverse_1(root.left)
        self.node_vals_1.append(root.val)
        self.traverse_1(root.right)
    
    def traverse_2(self, root):

        if(root == None):
            return

        self.traverse_2(root.left)
        self.node_vals_2.append(root.val)
        self.traverse_2(root.right)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        self.traverse_1(root1)
        self.traverse_2(root2)

        out_arr = []

        while(True):

            try:
                if(self.node_vals_1[0] <= self.node_vals_2[0]):
                    out_arr.append(self.node_vals_1.pop(0))
                else:
                    out_arr.append(self.node_vals_2.pop(0))

            except:
                break
        
        if(len(self.node_vals_1) != 0):
            out_arr += self.node_vals_1
        else:
            out_arr += self.node_vals_2


        return out_arr