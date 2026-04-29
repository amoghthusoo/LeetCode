# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:

        node_list = []

        ptr = head
        while(ptr != None):
            node_list.append(ptr)
            ptr = ptr.next

        
        while(True):

            break_mem = False
            outer_loop_break = False
            i = 0
            while(i < len(node_list)):
                j = i
                temp_sum = 0
                while(j < len(node_list)):
                    temp_sum += node_list[j].val                
                    
                    if(temp_sum == 0):
                        del node_list[i : j + 1]
                        outer_loop_break = True
                        break
                    j += 1
                
                if(outer_loop_break):
                    break
                
                i += 1

            if(i == j == len(node_list) or len(node_list) == 0):
                break
        
        if(len(node_list) == 0):
            return None
        
        i = 0
        while(i < len(node_list) - 1):
            node_list[i].next = node_list[i + 1]
            i += 1

        node_list[-1].next = None

        return node_list[0]

head = ListNode(1, ListNode(0, ListNode(1, ListNode(0, ListNode(2)))))
obj = Solution()
result = obj.removeZeroSumSublists(head)
print(result)
    