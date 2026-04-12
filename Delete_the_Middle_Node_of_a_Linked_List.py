# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def deleteMiddle(self, head: ListNode) -> ListNode:
        
        node_list = []
        ptr = head
        while(ptr != None):
            node_list.append(ptr)
            ptr = ptr.next

        delete_index = len(node_list) // 2

        if(len(node_list) == 1):
            return None

        node_list[delete_index - 1].next = node_list[delete_index].next

        return node_list[0]
