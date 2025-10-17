# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def insertAtEnd(self, head, tail, val):
        
        temp = ListNode(val)

        if(head == tail == None):
            head = tail = temp
        
        else:
            tail.next = temp
            tail = temp
        
        return head, tail

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        head, tail = None, None
        h1 = list1
        h2 = list2

        while(h1 != None and h2 != None):
            
            if(h1.val <= h2.val):
                head, tail = self.insertAtEnd(head, tail, h1.val)
                h1 = h1.next
            else:
                head, tail = self.insertAtEnd(head, tail, h2.val)
                h2 = h2.next

        while(h1 != None):
            head, tail = self.insertAtEnd(head, tail, h1.val)
            h1 = h1.next
        
        while(h2 != None):
            head, tail = self.insertAtEnd(head, tail, h2.val)
            h2 = h2.next
        
        return head

        