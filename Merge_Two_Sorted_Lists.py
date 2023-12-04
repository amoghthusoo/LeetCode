class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:

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

    def listToLinkedList(self, inList):
        
        outHead = None

        for element in inList:
            outHead = self.insertAtEnd(outHead, element)

        return outHead

    def insertSorted(self, head, val):
        
        temp = ListNode()
        temp.val = val
        temp.next = None

        if(head == None):
            head = temp
            return head
        
        elif(head.next == None):
            
            if(val <= head.val):
                temp.next = head
                head = temp
            else:
                head.next = temp
            return head
        
        elif(val <= head.val):
            temp.next = head
            head = temp

            return head
        
        else:

            traversePtr = head
            while(traversePtr.next != None):

                if(val <= traversePtr.next.val):
                    temp.next = traversePtr.next
                    traversePtr.next = temp
                    return head
                
                traversePtr = traversePtr.next

            traversePtr.next = temp
            return head
            
    def sortLinkedList(self, head):
        
        outHead = None

        traversePtr = head

        while(traversePtr != None):
            outHead = self.insertSorted(outHead, traversePtr.val)
            traversePtr = traversePtr.next

        return outHead
            
    def showLinkedList(self, head):

        while(head != None):
            print(f"{head.val} -> ", end="")
            head = head.next

        print(None)

class Solution:
    def mergeTwoLists(self, list1, list2):
        
        linkedListOperations = LinkedList()
        outHead = None

        traversePtr = list1
        while(traversePtr != None):
            outHead = linkedListOperations.insertSorted(outHead, traversePtr.val)
            traversePtr = traversePtr.next

        traversePtr = list2

        while(traversePtr != None):
            outHead = linkedListOperations.insertSorted(outHead, traversePtr.val)
            traversePtr = traversePtr.next

        return outHead
            
linkedListOperations = LinkedList()
list1 = []
list2 = [0]
list1 = linkedListOperations.listToLinkedList(list1)
list2 = linkedListOperations.listToLinkedList(list2)
obj = Solution()
out = obj.mergeTwoLists(list1, list2)
linkedListOperations.showLinkedList(out)