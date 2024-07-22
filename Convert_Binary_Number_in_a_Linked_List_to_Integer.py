# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head) -> int:

        bin_str = ""

        traversePtr = head
        while(traversePtr != None):

            bin_str += str(traversePtr.val)

            traversePtr = traversePtr.next

        return int(bin_str, 2)
