# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        if(head == None):
            return None
        
        strictly_smaller = []
        equal_larger = []

        ptr = head
        while(ptr != None):

            if(ptr.val < x):
                strictly_smaller.append(ptr)
            else:
                equal_larger.append(ptr)

            ptr = ptr.next
        
        strictly_smaller.extend(equal_larger)

        i = 0
        while(i < len(strictly_smaller) - 1):
            
            strictly_smaller[i].next = strictly_smaller[i + 1]
            i += 1
        
        strictly_smaller[-1].next = None

        return strictly_smaller[0]
        
head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
x = 3
obj = Solution()
result = obj.partition(head, x)
print(result)

