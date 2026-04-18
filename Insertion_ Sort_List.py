# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        node_list = []

        ptr = head
        while(ptr != None):
            node_list.append(ptr)
            ptr = ptr.next

        
        i = 1
        while(i < len(node_list)):

            if(node_list[i].val < node_list[i - 1].val):

                temp = node_list[i].val
                j = i - 1
                while(j >= 0 and node_list[j].val >= temp):
                    node_list[j + 1].val = node_list[j].val
                    j -= 1
                
                node_list[j + 1].val = temp

            i += 1
        
        return node_list[0]
        