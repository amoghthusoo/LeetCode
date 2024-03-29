# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def getInorderTraversal(self, root : TreeNode, inorderTraversal : list[int]) -> None:
        
        if(root == None):
            return
        else:
            self.getInorderTraversal(root.left, inorderTraversal)
            
            inorderTraversal.append(root)
        
            self.getInorderTraversal(root.right, inorderTraversal)



    def isSymmetric(self, root: TreeNode) -> bool:  
        
        inorderTraversal = []
        self.getInorderTraversal(root, inorderTraversal)

        try:
            while(True):

                leftNode : TreeNode = inorderTraversal.pop(0)
                rightNode : TreeNode = inorderTraversal.pop()

                if(leftNode.val != rightNode.val):
                    return False
                
                elif(leftNode.left == None and rightNode.right != None):
                    return False
                
                elif(leftNode.left != None and rightNode.right == None):
                    return False
                
                elif(leftNode.right == None and rightNode.left != None):
                    return False
                
                elif(leftNode.right != None and rightNode.left == None):
                    return False

                elif(leftNode.left != None and rightNode.right != None):
                    
                    if(leftNode.left.val != rightNode.right.val):
                        return False
                
                elif(leftNode.right != None and rightNode.left != None):

                    if(leftNode.right.val != rightNode.left.val):
                        return False
                
        except:
            return True
    
        

# root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
root = TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(4)))
obj = Solution()
out = obj.isSymmetric(root)
print(out)