# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        node_dict = {}
        
        traversePtr = headA
        while(traversePtr != None):

            node_dict[traversePtr] = None
            traversePtr = traversePtr.next

        traversePtr = headB
        while(traversePtr != None):

            if(traversePtr in node_dict):
                return traversePtr
            
            traversePtr = traversePtr.next

        return None
