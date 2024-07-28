# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        traversePtr = head

        try:
            while(traversePtr.next != None):

                while(traversePtr.next.val == val):
                    traversePtr.next = traversePtr.next.next

                traversePtr = traversePtr.next

            try:
                while(head.val == val):
                    head = head.next
            except:
                return head

            return head
        
        except:

            try:
                while(head.val == val):
                    head = head.next
            except:
                return head

            return head
        
            