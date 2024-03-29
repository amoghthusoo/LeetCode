# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        linkedList_1 : list[ListNode]= []
        linkedList_2 : list[ListNode] = []

        traversePtr = list1
        while(traversePtr != None):
            linkedList_1.append(traversePtr)
            traversePtr = traversePtr.next

        traversePtr = list2
        while(traversePtr != None):
            linkedList_2.append(traversePtr)
            traversePtr = traversePtr.next

        linkedList_1[a - 1].next = linkedList_2[0]
        linkedList_2[-1].next = linkedList_1[b + 1]

        return linkedList_1[0]


list1 = [10,1,13,6,9,5]
a = 3
b = 4
list2 = [1000000,1000001,1000002]