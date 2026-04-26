# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if(head == None or head.next == None or head.next.next == None):
            return head
        
        odd_head = head
        even_head = head.next

        ptr_odd = odd_head
        ptr_even = even_head

        odd_larger = None

        while(True):

            try:
                ptr_odd.next = ptr_odd.next.next
                ptr_odd = ptr_odd.next

                
            except:
                pass

            try:
                ptr_even.next = ptr_even.next.next
                ptr_even = ptr_even.next
            except:
                pass

                

            if(ptr_odd.next == None):
                odd_larger = True
                break

            if(ptr_even.next == None):
                odd_larger = False
                break

        if(odd_larger):
            ptr_odd.next = even_head
        else:
            ptr_even.next = None
            ptr_odd.next = even_head

        return odd_head
            
        