# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        val_list = []
        traversePtr = head
        while(traversePtr != None):
            val_list.append(traversePtr.val)
            traversePtr = traversePtr.next

        val_list.sort()

        i = 0
        traversePtr = head
        while(traversePtr != None):
            traversePtr.val = val_list[i]
            traversePtr = traversePtr.next
            i += 1


        return head