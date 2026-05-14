# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.map = dict()
        self.levels = []

    def bfs(self, root):

        queue = [root]

        while(queue):

            level = []
            n = len(queue)
            for _ in range(n):

                node = queue.pop(0)
                level.append(node.val)

                if(node.left != None):
                    queue.append(node.left)
                
                if(node.right != None):
                    queue.append(node.right)

            self.levels.append(level)        

    def traverse(self, root):
        
        if(root == None):
            return 

        if(root.left != None):
            self.map[root.left.val] = root.val
        
        if(root.right != None):
            self.map[root.right.val] = root.val

        self.traverse(root.left)
        self.traverse(root.right)

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        self.map[root.val] = None
        self.traverse(root)
        self.bfs(root)

        if(self.map[x] == self.map[y]):
            return False
        else:
            
            for level in self.levels:

                if(x in level and y in level):
                    return True
            
            return False