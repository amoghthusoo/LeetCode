# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        visisted = set()

        ptr = head
        while(ptr != None):
            if(ptr not in visisted):
                visisted.add(ptr)
            else:
                return ptr
            
            ptr = ptr.next

        return None