from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def bfs(self, root):
        
        queue = deque([root])
        level_sum = []

        while(queue):

            _sum = 0
            n = len(queue)
            for _ in range(len(queue)):

                node = queue.popleft()
                _sum += node.val

                if(node.left is not None):
                    queue.append(node.left)

                if(node.right is not None):
                    queue.append(node.right)

            level_sum.append(_sum)
        
        return level_sum
    
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        
        level_sum = self.bfs(root)
        level_sum.sort()

        if(k > len(level_sum)):
            return -1
        else:
            return level_sum[-k]
