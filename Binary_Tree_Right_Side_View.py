from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def bfs(self, root):

        ans = []        
        queue = deque([root])

        while(queue):

            n = len(queue)
            for i in range(n):

                node = queue.popleft()

                if(node.left != None):
                    queue.append(node.left)
                
                if(node.right != None):
                    queue.append(node.right)

                if(i == n - 1):
                    ans.append(node.val)

        return ans

    def rightSideView(self, root: TreeNode) -> list[int]:
        
        if(root == None):
            return []
        
        return self.bfs(root)