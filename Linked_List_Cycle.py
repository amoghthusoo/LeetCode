# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

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
    def hasCycle(self, head) -> bool:
        
        referenceList = []

        traversePtr = head
        while(traversePtr != None):
            
            if(traversePtr not in referenceList):
                referenceList.append(traversePtr)
            else:
                return True
            
            traversePtr = traversePtr.next

        
        return False

_list = [3,2,0,-4]
pos = 1

head = None
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(-4)


head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = None

n1 = n2 = n3 = n4 = None

obj = Solution()
out = obj.hasCycle(head)
print(out)