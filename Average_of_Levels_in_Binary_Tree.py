# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def bfs(self, root):
        
        levels = []
        queue = [root]

        while(len(queue) != 0):

            temp = []
            n = len(queue)
            for _ in range(n):

                node = queue.pop(0)
                temp.append(node.val)
                
                if(node.left != None):
                    queue.append(node.left)
                
                if(node.right != None):
                    queue.append(node.right)
                
            levels.append(temp)

        return levels
    
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        
        levels = self.bfs(root)

        ans = []

        for level in levels:
            ans.append(sum(level)/len(level))
        
        return ans