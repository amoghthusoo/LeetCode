from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def bfs(self, root):

        levels = []
        queue = deque([root])
        while(queue):

            level = []
            n = len(queue)
            for _ in range(n):

                node = queue.popleft()
                level.append(node.val)

                if(node.left != None):
                    queue.append(node.left)
                
                if(node.right != None):
                    queue.append(node.right)
            
            levels.append(level)

        return levels

        
    def isEvenOddTree(self, root: TreeNode) -> bool:
        
        levels = self.bfs(root)

        i = 0
        while(i < len(levels)):

            expected_r = (i % 2) ^ 1
            j = 0
            while(j < len(levels[i])):

                if(levels[i][j] % 2 != expected_r):
                    return False
                
                if(i % 2 == 0):
                    try:
                        if(levels[i][j] >= levels[i][j + 1]):
                            return False
                    except:
                        pass
                else:
                    try:
                        if(levels[i][j] <= levels[i][j + 1]):
                            return False
                    except:
                        pass

                j += 1

            i += 1

        return True