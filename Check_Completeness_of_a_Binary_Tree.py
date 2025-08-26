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
                level.append(node)

                if(node.left != None):
                    queue.append(node.left)
                
                if(node.right != None):
                    queue.append(node.right)
                
            levels.append(level)

        return levels 


    def isCompleteTree(self, root: TreeNode) -> bool:
        
        levels = self.bfs(root)

        i = 0
        while(i < len(levels) - 1):

            if(len(levels[i]) != 2 ** i):
                return False

            i += 1

        i -= 1

        last_level = []
        j = 0
        while(j < len(levels[i])):

            last_level.append(levels[i][j].left)
            last_level.append(levels[i][j].right)

            j += 1

        gap_mem = False
        i = 0
        for node in last_level:

            if(not gap_mem and node == None):
                gap_mem = True
                continue

            if(gap_mem and node != None):
                return False

        return True