# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.main_root = None
        self.permission = True
        self.key = None
        self.case = None
        self.terminate = False
        self.min = int(10 ** 5) + 1

    def find_case(self, root):

        if(self.case != None or root == None):
            return
        

        if(root.val == self.key):

            if(root.right == root.left == None):
                self.case = 0
            
            elif(
                (root.left == None and root.right != None) or
                (root.left != None and root.right == None)
                ):
                self.case = 1

            else:
                self.case = 2
            
            return
            
        self.find_case(root.left)
        self.find_case(root.right)

    def delete_node_0(self, root):

        if(self.terminate or root == None):
            return 

        if(root.left != None and root.left.val == self.key):
            root.left = None
            self.terminate = True
            return
        
        elif(root.right != None and root.right.val == self.key):
            root.right = None
            self.terminate = True
            return

        self.delete_node_0(root.left)
        self.delete_node_0(root.right)

    def delete_node_1(self, root):
        
        if(self.terminate or root == None):
            return 
        
        if(root.val == self.key):

            if(root.left != None):
                self.main_root = root.left
            else:
                self.main_root = root.right
        
        if(root.left != None and root.left.val == self.key):
            
            if(root.left.left != None):
                root.left = root.left.left
            
            else:
                root.left = root.left.right

            self.terminate = True
            return 

        elif(root.right != None and root.right.val == self.key):
            
            if(root.right.left != None):
                root.right = root.right.left
            
            else:
                root.right = root.right.right


            self.terminate = True
            return

        self.delete_node_1(root.left)
        self.delete_node_1(root.right)


    def delete_node_2(self, root):
        
        if(self.terminate or root == None):
            return
        
        if(root.val == self.key):

            self.find_min(root.right)        

            self.case = None
            self.terminate = False
            self.deleteNode(self.main_root, self.min)
            root.val = self.min

            self.terminate = True
            return

        self.delete_node_2(root.left)
        self.delete_node_2(root.right)

    
    def find_min(self, root):
        
        if(root == None):
            return
        
        if(root.val < self.min):
            self.min = root.val

        self.find_min(root.left)
        self.find_min(root.right)


    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        if(self.permission):
            self.main_root = root
            self.permission = False

        self.key = key
        self.find_case(root)

        if(self.case == None):
            return root
        
        if(self.case == 0):

            if(root.val == self.key):
                return None
            self.delete_node_0(root)

        elif(self.case == 1):
            self.delete_node_1(root)
        
        else:
            self.delete_node_2(root)

        return self.main_root


# root = TreeNode(
#     5,
#     TreeNode(
#         3,
#         TreeNode(2),
#         TreeNode(4)
#     ),
#     TreeNode(
#         6,
#         None,
#         TreeNode(7)
#     )
# )
root = TreeNode(
    1,
    None,
    TreeNode(2)
)
key = 1

obj = Solution()
result = obj.deleteNode(root, key)
print(result)