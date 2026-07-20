# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str):
        
        parsed = []
        dash_cnt = 0
        

        i = 0
        while(i < len(traversal)):

            dash_cnt = 0
            while(i < len(traversal) and traversal[i] == "-"):
                dash_cnt += 1
                i += 1
            
            num = ""
            while(i < len(traversal) and traversal[i] != "-"):
                num += traversal[i]
                i += 1
            
            parsed.append((int(num), dash_cnt))


        root = TreeNode(parsed[0][0])
        stack = [(parsed[0][0], parsed[0][1], root)]

        i = 1
        while(i < len(parsed)):

            val = parsed[i][0]
            depth = parsed[i][1]


            if(depth < len(stack)):
                
                while(depth != len(stack)):
                    stack.pop()

            parent = stack[-1][-1]
            child = TreeNode(val)                
            if(parent.left == None):
                parent.left = child
            else:
                parent.right = child
            
            stack.append((val, depth, child))

            i += 1
        
        return root


traversal = "1-401--349---90--88"
obj = Solution()
result = obj.recoverFromPreorder(traversal)
print(result)
        

