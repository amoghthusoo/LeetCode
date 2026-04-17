
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:

    def __init__(self):
        self.head = None
        self.rear = None

    def insertAtEnd(self, val):
        
        temp = Node()
        temp.prev = temp.next = temp.child = None
        temp.val = val

        if(self.head == self.rear == None):
            self.head = self.rear = temp
        else:
            temp.prev = self.rear
            self.rear.next = temp
            self.rear = temp

    def traverse(self, head):
        
        ptr = head
        while(ptr != None):
            self.insertAtEnd(ptr.val)

            if(ptr.child != None):
                self.traverse(ptr.child)

            ptr = ptr.next

    def flatten(self, head: Node) -> Node:
        
        self.traverse(head)
        return self.head