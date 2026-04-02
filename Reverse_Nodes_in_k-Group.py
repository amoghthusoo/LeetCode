# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        node_list = []

        ptr = head
        while(ptr != None):
            node_list.append(ptr)
            ptr = ptr.next

        x = 0
        y = k - 1

        while(y < len(node_list)):
            i = x
            j = y

            while(i < j):
                node_list[i].val, node_list[j].val = node_list[j].val, node_list[i].val
                i += 1
                j -= 1

            x += k
            y += k
        
        return node_list[0]