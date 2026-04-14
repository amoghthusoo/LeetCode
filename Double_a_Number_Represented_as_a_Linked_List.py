import sys
sys.set_int_max_str_digits(100000)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def insertAtEnd(self, head, rear, val):

        temp = ListNode()
        temp.val = val
        
        if(head == rear == None):    
            head = rear = temp
            return head, rear
        
        rear.next = temp
        rear = temp

        return head, rear
    
    def doubleIt(self, head: ListNode) -> ListNode:

        num = ""
        ptr = head
        while(ptr != None):
            num += str(ptr.val)
            ptr = ptr.next

        num = str(int(num) * 2)

        head = rear = None
        for e in num:
            head, rear = self.insertAtEnd(head, rear, int(e))
        
        return head
