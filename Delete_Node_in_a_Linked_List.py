# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:

    def insertAtEnd(self, head, value):

        temp = ListNode(value)

        if(head == None):
            head = temp
        else:
            traversePtr = head
            while(traversePtr.next != None):
                traversePtr = traversePtr.next
            traversePtr.next = temp
        
        return head
    
    def getReference(self, head, target):

        traversePtr = head
        while(traversePtr.val != target):
            traversePtr = traversePtr.next
        
        return traversePtr

    def displayLinkedList(self, head):

        traversePtr = head
        while(traversePtr != None):
            print(traversePtr.val, "-> ", end = "")
            traversePtr = traversePtr.next

        print("None")

class Solution:

    def deleteNode(self, node):
        
        traversePtr = node
        while(True):

            traversePtr.val = traversePtr.next.val

            if(traversePtr.next.next == None):
                traversePtr.next = None
                break
            else:
                traversePtr = traversePtr.next

def main():

    head = None
    linked_list = LinkedList()

    head = linked_list.insertAtEnd(head, 4)
    head = linked_list.insertAtEnd(head, 5)
    head = linked_list.insertAtEnd(head, 1)
    head = linked_list.insertAtEnd(head, 9)

    linked_list.displayLinkedList(head)

    node = linked_list.getReference(head, 1)

    solution_obj = Solution()
    solution_obj.deleteNode(node)

    linked_list.displayLinkedList(head)

if(__name__ == "__main__"):
    print()
    main()
    print()

