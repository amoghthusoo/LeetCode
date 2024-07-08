# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from math import gcd

class Solution:
    def insertGreatestCommonDivisors(self, head):
        
        traversePtr = head

        while(traversePtr.next != None):

            temp = ListNode(gcd(traversePtr.val, traversePtr.next.val))

            temp.next = traversePtr.next
            traversePtr.next = temp


            traversePtr = traversePtr.next.next

        return head
        


