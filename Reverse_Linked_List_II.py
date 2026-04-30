# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        node_list = []
        ptr = head
        while(ptr != None):
            node_list.append(ptr)
            ptr = ptr.next

        i = left - 1
        j = right - 1

        while(i < j):
            node_list[i].val, node_list[j].val = node_list[j].val, node_list[i].val
            i += 1
            j -= 1
        
        return node_list[0]
        