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
    
    def isPalindrome(self, head : ListNode) -> bool:
        
        inter_list_1 = []
        inter_list_2 = []

        traversePtr = head
        while(traversePtr != None):

            inter_list_1.append(traversePtr.val)
            inter_list_2.insert(0, traversePtr.val)

            traversePtr = traversePtr.next

        if(inter_list_1 == inter_list_2):
            return True
        else:
            return False

def main():
    head = None
    linked_list = LinkedList()

    head = linked_list.insertAtEnd(head, 1)
    head = linked_list.insertAtEnd(head, 2)
    # head = linked_list.insertAtEnd(head, 2)
    # head = linked_list.insertAtEnd(head, 1)

    linked_list.displayLinkedList(head)
    obj = Solution()
    out = obj.isPalindrome(head)
    print(out)

if(__name__ == "__main__"):
    print()
    main()
    print()
