# Definition for a Node.
class Node:
    def __init__(self, val = None, children = None):
        self.val = val
        self.children = children


class Solution:

    def __init__(self):
        self.ans = []

    def traverse(self, root):
        if(root == None):
            return
        
        for child in root.children:
            self.traverse(child)

        self.ans.append(root.val)

    def postorder(self, root: Node) -> list[int]:
        
        self.traverse(root)
        return self.ans
