from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.arr = []

        queue = deque([root])

        while(queue):

            n = len(queue)
            for _ in range(n):

                node = queue.popleft()
                self.arr.append(node)

                if(node.left != None):
                    queue.append(node.left)
                
                if(node.right != None):
                    queue.append(node.right)
        

    def insert(self, val: int) -> int:
        
        self.arr.append(TreeNode(val))

        if(len(self.arr) > 1):

            child_index = len(self.arr) - 1
            if(child_index % 2 == 0):
                parent = self.arr[(child_index - 2) // 2]
                parent.right = self.arr[child_index]
            else:
                parent = self.arr[(child_index - 1) // 2]
                parent.left = self.arr[child_index]

        return parent.val

    def get_root(self) -> TreeNode:
        
        if(self.arr):
            return self.arr[0]
        else:
            return None


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()