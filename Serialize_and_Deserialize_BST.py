# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def __init__(self):
        self.str = ""

    def inorder(self, root):

        if(root == None):
            return
        
        self.inorder(root.left)
        self.str += f"{root.val},{id(root)} "
        # self.str += str(root.val) + " "
        self.inorder(root.right)
    
    def postorder(self, root):

        if(root == None):
            return
        
        self.postorder(root.left)
        self.postorder(root.right)
        self.str += f"{root.val},{id(root)} "
        # self.str += str(root.val) + " "

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.str = ""

        self.inorder(root)
        self.postorder(root)

        return self.str
    

    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:

        if(len(inorder) == 0):
            return None
        
        root = postorder.pop()
        root_index = inorder.index(root)

        left_inorder = inorder[0 : root_index]
        right_inorder = inorder[root_index + 1 : ]

        left_postorder = postorder[0 : len(left_inorder)]
        right_postorder = postorder[len(left_inorder) : ]

        root_val = int(root.split(",")[0])
        root_node = TreeNode(root_val)
        root_node.left = self.buildTree(left_inorder, left_postorder)
        root_node.right = self.buildTree(right_inorder, right_postorder)

        return root_node
        

    def deserialize(self, data : str):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        data = data.split()
        inorder = []
        postorder = []

        i = 0
        while(i < len(data)//2):
            
            inorder.append(data[i])
            
            i += 1
        
        while(i < len(data)):

            postorder.append(data[i])

            i += 1

        return self.buildTree(inorder, postorder)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))