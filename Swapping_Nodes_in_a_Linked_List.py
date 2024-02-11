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
    def swapNodes(self, head, k: int): #returns head
        
        referenceList = []      # List of references of each node in order
        traversePtr = head

        while(traversePtr != None):
            referenceList.append(traversePtr)
            traversePtr = traversePtr.next

        referenceListLen = len(referenceList)
        referenceList[k - 1].val, referenceList[referenceListLen - k].val = referenceList[referenceListLen - k].val, referenceList[k - 1].val 

        return head

        


_list = [7,9,6,6,7,8,3,0,9,5]
k = 5

operationObj = LinkedListOperations()
head = operationObj.listToLinkedList(_list)

obj = Solution()
out = obj.swapNodes(head, k)
operationObj.displayLinkedList(out)
