class ListNode:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.size = 100
        self.hashmap = [None for _ in range(self.size)]

    def insertAtStart(self, head, value):
        
        temp = ListNode(value)

        if(head == None):
            head = temp
        else:
            temp.next = head
            head = temp

        return head
    
    def updateValue(self, head, key, value):

        traversePtr = head
        while(traversePtr != None):

            if(traversePtr.val[0] == key):
                traversePtr.val[1] = value

            traversePtr = traversePtr.next

    def exists(self, key):

        index = key % self.size

        if(self.hashmap[index] == None):
            return False
        
        else:
            traversePtr = self.hashmap[index]

            while(traversePtr != None):

                if(traversePtr.val[0] == key):
                    return True
                
                traversePtr = traversePtr.next

            return False
        
    def removeSpecific(self, head, target):

        if(head == None):
            return None
        
        elif(head.val[0] == target):
            return head.next


        traversePtr = head

        while(traversePtr.next != None):

            if(traversePtr.next.val[0] == target):
                traversePtr.next = traversePtr.next.next
                break

            traversePtr = traversePtr.next

        return head
    

    def put(self, key: int, value: int) -> None:
        
        index = key % self.size

        if(not self.exists(key)):
            self.hashmap[index] = self.insertAtStart(self.hashmap[index], [key, value])   
        
        else:
            self.updateValue(self.hashmap[index], key, value)

    
            

    def get(self, key: int) -> int:

        if(not self.exists(key)):
            return -1

        else:

            index = key % self.size
            traversePtr = self.hashmap[index]

            while(traversePtr != None):

                if(traversePtr.val[0] == key):
                    return traversePtr.val[1]
                
                traversePtr = traversePtr.next

    def remove(self, key: int) -> None: 
        
        index = key % self.size
        self.hashmap[index] = self.removeSpecific(self.hashmap[index], key)
