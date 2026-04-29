# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.max = -1
        self.valid_nodes = []

    def traverse(self, head):

        if(head.next == None):
            self.max = head.val
            self.valid_nodes.append(head)
            return
        
        self.traverse(head.next)

        if(head.val >= self.max):
            self.valid_nodes.append(head)
            self.max = head.val    
        

    def removeNodes(self, head: ListNode) -> ListNode:

        self.traverse(head)

        if(len(self.valid_nodes) == 0):
            return None

        i = len(self.valid_nodes) - 1
        while(i >= 1):
            
            self.valid_nodes[i].next = self.valid_nodes[i - 1]
            i -= 1    

        return self.valid_nodes[-1]
    


        