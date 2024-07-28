import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:

    def __init__(self, head: ListNode):
        
        self.node_list = []

        traversePtr = head
        while(traversePtr != None):
            self.node_list.append(traversePtr)
            traversePtr = traversePtr.next

    def getRandom(self) -> int:

        return random.choice(self.node_list).val