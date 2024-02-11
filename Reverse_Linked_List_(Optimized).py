class ListNode:

    def __init__(self, val=0, next=None):
        self.val = None
        self.next = None

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
        

class Solution:
    def reverseList(self, head):
        
        linkedListOperations = LinkedList()        
        head = linkedListOperations.reverseLinkedList(head)
        return head

linkedListOperations = LinkedList()
_list = []
head = linkedListOperations.listToLinkedList(_list)
obj = Solution()
out = obj.reverseList(head)
linkedListOperations.showLinkedList(out)