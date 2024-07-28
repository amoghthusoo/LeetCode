# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        traversePtr = head

        try:
            while(traversePtr.next != None):

                while(traversePtr.val == traversePtr.next.val):
                    traversePtr.next = traversePtr.next.next


                traversePtr = traversePtr.next
        except:
            return head

        return head