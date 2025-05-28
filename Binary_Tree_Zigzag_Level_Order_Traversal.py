# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        
        if(root == None):
            return []
        
        queue = [root]
        bfs = []    
        depth = 0

        while(len(queue) != 0):

            level = []
            n = len(queue)
            for _ in range(n):

                node = queue.pop(0)

                if(depth % 2 == 0):
                    level.append(node.val)
                else:
                    level.insert(0, node.val)

                if(node.left != None):
                    queue.append(node.left)
                
                if(node.right != None):
                    queue.append(node.right)

            depth += 1
            bfs.append(level)

        return bfs

root = TreeNode(
    3, 
    TreeNode(9),
    TreeNode(
        20,
        TreeNode(15),
        TreeNode(7)
    )
)

solution = Solution()
result = solution.zigzagLevelOrder(root)
print(result)