# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
    

    def displayLinkedList(self, head):

        traversePtr = head
        while(traversePtr != None):
            print(traversePtr.val, "-> ", end = "")
            traversePtr = traversePtr.next

        print("None")

class Solution:
    def middleNode(self, head):
        
        inter_list = []

        traversePtr = head
        while(traversePtr != None):
            inter_list.append(traversePtr)
            traversePtr = traversePtr.next

        if(len(inter_list) % 2 == 0):
            return inter_list[len(inter_list)//2]
        else:
            return inter_list[len(inter_list)//2]    

def main():

    head = None
    linked_list = LinkedList()

    head = linked_list.insertAtEnd(head, 1)
    head = linked_list.insertAtEnd(head, 2)
    head = linked_list.insertAtEnd(head, 3)
    head = linked_list.insertAtEnd(head, 4)
    head = linked_list.insertAtEnd(head, 5)
    head = linked_list.insertAtEnd(head, 6)
    
    linked_list.displayLinkedList(head)

    obj = Solution()
    out = obj.middleNode(head)
    
    linked_list.displayLinkedList(out)

if(__name__ == "__main__"):
    print()
    main()
    print()