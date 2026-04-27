
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    
    def bfs(self, root):
        
        queue = [root]
        bfs = []

        while(len(queue) != 0):

            temp = []
            n = len(queue)
            for _ in range(n):
                
                node = queue.pop(0)
                temp.append(node)

                if(node.left != None):
                    queue.append(node.left)
                
                if(node.right != None):
                    queue.append(node.right)
            
            bfs.append(temp)

        return bfs

    def connect(self, root: 'Node') -> 'Node':
        if(root == None):
            return None
        
        levels = self.bfs(root)

        for level in levels:
            i = 0
            while(i < len(level) - 1):
                
                level[i].next = level[i + 1]
                i += 1

        return levels[0][0]
        