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

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        num1 = ""
        ptr = l1
        while(ptr != None):
            num1 += str(ptr.val)
            ptr = ptr.next
        
        num2 = ""
        ptr = l2
        while(ptr != None):
            num2 += str(ptr.val)
            ptr = ptr.next
        
        _sum = str(int(num1) + int(num2))

        head = rear = None
        for e in _sum:
            head, rear = self.insertAtEnd(head, rear, int(e))
        
        return head