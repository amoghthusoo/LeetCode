
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

    def reverseLinkedList(self, head):

        outHead = None

        if(head == None):
            return outHead
        
        while True:

            traversePtr = head 
            
            if(traversePtr.next == None):
                outHead = self.insertAtEnd(outHead, traversePtr.val)
                return outHead

            while(traversePtr.next.next != None):
                traversePtr = traversePtr.next

            outHead = self.insertAtEnd(outHead, traversePtr.next.val)
            traversePtr.next = None

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

            


linkedListOperations = LinkedList()
obj = LinkedList()
head = None

head = linkedListOperations.insertSorted(head, 4)
head = linkedListOperations.insertSorted(head, 2)
head = linkedListOperations.insertSorted(head, 1)
head = linkedListOperations.insertSorted(head, 3)

obj.showLinkedList(head)

print()
