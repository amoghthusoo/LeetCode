class ListNode:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.len = 0

    def get(self, index: int) -> int:
        
        if(index >= self.len):
            return -1
        
        traversePtr = self.head
        i = 0
        while(i < index):
            traversePtr = traversePtr.next
            i += 1

        return traversePtr.val            

    def addAtHead(self, val: int) -> None:

        temp = ListNode(val)
        temp.next = self.head
        self.head = temp
        self.len += 1
                

    def addAtTail(self, val: int) -> None:
        
        temp = ListNode(val)

        if(self.head == None):
            self.head = temp
            self.len += 1
            return

        traversePtr = self.head

        while(traversePtr.next != None):
            traversePtr = traversePtr.next
        
        traversePtr.next = temp
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        
        if(index > self.len):
            return
    
        if(index == self.len):
            self.addAtTail(val)
            return
        
        if(index == 0):
            self.addAtHead(val)
            return
        
        traversePtr = self.head
        i = 0
        while(i < index - 1):
            traversePtr = traversePtr.next
            i += 1

        temp = ListNode(val)
        temp.next = traversePtr.next
        traversePtr.next = temp
        self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        
        if(index >= self.len):
            return
        

        if(index == 0):
            self.head = self.head.next
            self.len -= 1
            return
        
        traversePtr = self.head
        i = 0
        while(i < index - 1):
            traversePtr = traversePtr.next
            i += 1

        traversePtr.next = traversePtr.next.next
        self.len -= 1
        



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)