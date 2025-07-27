from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: TreeNode) -> list[int]:

        if(root == None):
            return []
        
        ans = []
        queue = deque([root])

        while(queue):

            max_val = -(2 ** 31) - 1
            n = len(queue)
            for _ in range(n):

                node = queue.popleft()
                
                if(node.val > max_val):
                    max_val = node.val

                if(node.left != None):
                    queue.append(node.left)
                
                if(node.right != None):
                    queue.append(node.right)

            ans.append(max_val)

        return ans