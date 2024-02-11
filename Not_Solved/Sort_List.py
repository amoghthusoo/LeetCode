class ListNode:

    def __init__(self, val=0, next=None):
        self.val = None
        self.next = None

class LinkedList:

    def insertAtStart(self, head, val):
  
        temp = ListNode()
        temp.val = val
        temp.next = head
        head = temp
        
        return head
    
    def insertAtEnd(self, head, val):
        
        temp = ListNode()
        temp.val = val
        temp.next = None

        if(head == None):
            head = temp
        else:
            traversePtr = head
            
            while(traversePtr.next != None):
                traversePtr = traversePtr.next

            traversePtr.next = temp
        
        return head
    
    def linkedListToList(self, head):

        outList = []

        traversePtr = head
        while(traversePtr != None):
            
            outList.append(traversePtr.val)
            traversePtr = traversePtr.next
        
        return outList
    
    def listToLinkedList(self, inList):
        
        outHead = None

        for element in inList:
            outHead = self.insertAtEnd(outHead, element)

        return outHead
            
    
    def showLinkedList(self, head):

        while(head != None):
            print(f"{head.val} -> ", end="")
            head = head.next

        print(None)


class Solution:

    def sortList(self, head):

        linkedListOperation = LinkedList()

        _list = linkedListOperation.linkedListToList(head)
        _list.sort()
        head = linkedListOperation.listToLinkedList(_list)

        return head

_list = []
linkedListOperation = LinkedList()
head = linkedListOperation.listToLinkedList(_list)
obj = Solution()
head = obj.sortList(head)
linkedListOperation.showLinkedList(head)
