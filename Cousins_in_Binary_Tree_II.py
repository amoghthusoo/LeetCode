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
        queue = deque([[root, None]])

        while(queue):
            
            level = []
            level_sum = 0
            n = len(queue)
            for _ in range(n):

                node = queue.popleft()
                node_ref = node[0]
                node_par = node[1]

                level.append(node)
                level_sum += node_ref.val

                if(node_ref.left != None):
                    queue.append([node_ref.left, node_ref])

                if(node_ref.right != None):
                    queue.append([node_ref.right, node_ref])

            levels.append([level, level_sum])
        
        return levels

    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        
        levels = self.bfs(root)
        
        mod_vals = []

        for l in levels:
            level = l[0]
            level_sum = l[1]
            
            temp = []
            for i, node in enumerate(level):
                node_ref = node[0]
                node_par = node[1]

                if(len(level) == 1):
                    temp.append(0)

                else:
                    sibling_sum = node_ref.val

                    try:
                        if(level[i + 1][1] == node_par):
                            sibling_sum += level[i + 1][0].val
                    except:
                        pass

                    
                    if(i != 0):
                        
                        try:
                            if(level[i - 1][1] == node_par):
                                sibling_sum += level[i - 1][0].val
                        except:
                            pass
                    
                    temp.append(level_sum - sibling_sum)
            
            mod_vals.append(temp)

        i = 0
        for l in levels:
            level = l[0]
            level_sum = l[1]

            j = 0
            for node in level:
                node_ref = node[0]
                node_par = node[1]
                
                node_ref.val = mod_vals[i][j]
                j += 1
            
            i += 1

        return root

    

root = TreeNode(
    5,
    TreeNode(
        4,
        TreeNode(1),
        TreeNode(10)
    ),
    TreeNode(
        9,
        None,
        TreeNode(7)
    )
)

obj = Solution()
result = obj.replaceValueInTree(root)
print(result)