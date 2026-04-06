# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    def insertAtEnd(self, head, tail, val):
        
        if(head == tail == None):
            head = tail = ListNode(val)
        else:
            temp = ListNode(val)
            tail.next = temp
            tail = temp

        return head, tail
    
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        occr_dict = dict()

        traversePtr = head
        while(traversePtr != None):

            if(traversePtr.val not in occr_dict):
                occr_dict[traversePtr.val] = 1
            else:
                occr_dict[traversePtr.val] += 1
            
            traversePtr = traversePtr.next

    
        head = tail = None
        for val, freq in occr_dict.items():
            if(freq == 1):
                head, tail = self.insertAtEnd(head, tail, val)

        return head        