class ListNode:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyHashSet:

    def insertAtStart(self, head, value):
        
        temp = ListNode(value)

        if(head == None):
            head = temp
        else:
            temp.next = head
            head = temp

        return head
    
    def exists(self, head, target):

        traversePtr = head
        
        while(traversePtr != None):
            if(traversePtr.val == target):
                return True
            
            traversePtr = traversePtr.next

        return False
    
    def removeSpecific(self, head, target):

        if(head == None):
            return None
        
        elif(head.val == target):
            return head.next

        traversePtr = head

        while(traversePtr.next != None):

            if(traversePtr.next.val == target):
                traversePtr.next = traversePtr.next.next
                break
            
            
            traversePtr = traversePtr.next

        return head

    def __init__(self):
        self.size = 100
        self.hashset = [None for _ in range(self.size)]

    def add(self, key: int) -> None:

        if(not self.contains(key)):
            index = key % self.size
            self.hashset[index] = self.insertAtStart(self.hashset[index], key)

    def remove(self, key: int) -> None:
        
        index = key % self.size
        self.hashset[index] = self.removeSpecific(self.hashset[index], key)

    def contains(self, key: int) -> bool:
        
        index = key % self.size
        return self.exists(self.hashset[index], key)

