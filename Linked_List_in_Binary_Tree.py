# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self):
        self.node_list = []
        self.found_mem = False

    def check_path(self, root):
        
        stack = []
        i = 0
        curr_node = root

        while(True):
            
            if(curr_node.val != self.node_list[i]):

                if(len(stack) != 0):
                    checkpoint = stack.pop()
                    curr_node = checkpoint[0]
                    i = checkpoint[1]
                    continue

                else:
                    return
            
            else:
                
                i += 1
                if(i == len(self.node_list)):
                    self.found_mem = True
                    return
                
                
                if(curr_node.left == curr_node.right == None):

                    if(len(stack) != 0):
                        checkpoint = stack.pop()
                        curr_node = checkpoint[0]
                        i = checkpoint[1]
                        continue

                    else:
                        return

            
                elif(curr_node.left != None and curr_node.right == None):
                    curr_node = curr_node.left
                
                
                elif(curr_node.left == None and curr_node.right != None):
                    curr_node = curr_node.right
                

                else:
                    stack.append([curr_node.right, i])
                    curr_node = curr_node.left
            
            
    def traverse(self, root):

        if(root == None):
            return
        
        if(root.val == self.node_list[0]):
            self.check_path(root)
        
        if(self.found_mem):
            return
        
        self.traverse(root.left)
        
        if(self.found_mem):
            return 

        self.traverse(root.right)

        if(self.found_mem):
            return False

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        
        ptr = head
        while(ptr != None):
            self.node_list.append(ptr.val)
            ptr = ptr.next
        
        self.traverse(root)
        return self.found_mem
        