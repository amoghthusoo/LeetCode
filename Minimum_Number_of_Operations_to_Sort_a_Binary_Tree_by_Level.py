from collections import deque
from sortedcontainers import SortedList

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
            sorted_level = SortedList()
            level_dict = {}

            n = len(queue)
            for _ in range(n):

                node = queue.popleft()

                level.append(node.val)
                sorted_level.add(node.val)
                level_dict[node.val] = len(level_dict)

                if(node.left != None):
                    queue.append(node.left)
                
                if(node.right != None):
                    queue.append(node.right)

            levels.append([level, sorted_level, level_dict])

        return levels

    def minimumOperations(self, root: TreeNode) -> int:

        swaps = 0        
        levels = self.bfs(root)
        
        for l in levels:
            level = l[0]
            sorted_level = l[1]
            level_dict = l[2]

            i = 0
            while(i < len(level)):

                if(level[i] != sorted_level[i]):

                    intended_element = sorted_level[i]
                    intended_element_index = level_dict[intended_element]
                    level_dict[level[i]], level_dict[sorted_level[i]] = level_dict[sorted_level[i]], level_dict[level[i]]
                    level[i], level[intended_element_index] = level[intended_element_index], level[i]
                    swaps += 1

                i += 1

        return swaps
    
root = TreeNode(
    1, 
    TreeNode(
        4,
        TreeNode(7),
        TreeNode(6)
    ),
    TreeNode(
        3,
        TreeNode(
            8,
            TreeNode(9)
        ),
        TreeNode(
            5,
            TreeNode(10)
        )
    )
)

obj = Solution()
result = obj.minimumOperations(root)
print(result)