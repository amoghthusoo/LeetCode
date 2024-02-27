# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListOperations:

    def insertAtEnd(self, head, element):
        
        temp = ListNode(element)

        if(head == None):
            head = temp
        else:
            traversePtr = head
            while(traversePtr.next != None):
                traversePtr = traversePtr.next
            
            traversePtr.next = temp
        
        return head

    def displayLinkedList(self, head):
        
        traversePtr = head
        while(traversePtr != None):
            print(traversePtr.val, end=" -> ")
            traversePtr = traversePtr.next
        print(None)

    def listToLinkedList(self, _list):
        head = None

        for element in _list:
            head = self.insertAtEnd(head, element)

        return head

class Solution:

    def insertAtEnd(self, head, element):
        
        temp = ListNode(element)

        if(head == None):
            head = temp
        else:
            traversePtr = head
            while(traversePtr.next != None):
                traversePtr = traversePtr.next
            
            traversePtr.next = temp
        
        return head
    
    def doubleIt(self, head):
        
        numStr = ""

        traversePtr = head
        while(traversePtr != None):
            numStr += str(traversePtr.val)
            traversePtr = traversePtr.next

        numStr = str(int(numStr) * 2)

        outHead = None

        for ch in numStr:
            outHead = self.insertAtEnd(outHead, int(ch))

        return outHead


_list = [9, 9, 9]
oprObj = LinkedListOperations()
head = oprObj.listToLinkedList(_list)

obj = Solution()
out = obj.doubleIt(head)
oprObj.displayLinkedList(out)