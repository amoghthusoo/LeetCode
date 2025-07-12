# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def get_bfs(self, root):
        
        if(root == None):
            return 0
        
        queue = [root]

        bfs = []

        while(len(queue) != 0):
            
            temp = []
            n = len(queue)
            for i in range(n):

                node = queue.pop(0)
                temp.append(node)

                if(node.left != None):
                    queue.append(node.left)

                if(node.right != None):
                    queue.append(node.right)

            bfs.insert(0, temp)
        
        return bfs

    def find(self, root, target):

        if(root == None):
            return False
        
        if(root.val == target):
            return True
        
        return self.find(root.left, target) or self.find(root.right, target)
    
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        bfs = self.get_bfs(root)
        deepest_leaves = [root.val for root in bfs[0]]

        for level in bfs:
            for node in level:

                found_mem = True
                for val in deepest_leaves:
                    if(self.find(node, val) == False):
                        found_mem = False
                        break

                if(found_mem == True):
                    return node