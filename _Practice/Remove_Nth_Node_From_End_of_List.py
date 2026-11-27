# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reference_list = []

        traversePtr = head
        while(traversePtr != None):

            reference_list.append(traversePtr)
            traversePtr = traversePtr.next

        if(len(reference_list) == 1):
            return None
        
        elif(n == len(reference_list)):
            return reference_list[1]
        
        elif(n == 1):
            reference_list[-2].next = None
            return reference_list[0]
        
        else:
            reference_list[-n-1].next = reference_list[-n + 1]
            return reference_list[0]