# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def insert_at_end(self, head, tail, val):

        temp = ListNode()
        temp.val = val

        if(head == tail == None):
            head = tail = temp
        
        else:
            tail.next = temp
            tail = temp
        
        return head, tail

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
        

        num1 = num1[-1::-1]
        num2 = num2[-1::-1]
        res = str(int(num1) + int(num2))
        res = res[-1::-1]
        

        head = None
        tail = None

        for e in res:
            head, tail = self.insert_at_end(head, tail, int(e))
        
        return head