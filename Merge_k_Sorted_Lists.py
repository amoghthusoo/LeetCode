# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def insertAtEnd(self, head, rear, element):

        if(head == rear == None):
            head = rear = ListNode(element, None)
            return head, rear
        
        temp = ListNode(element, None)
        rear.next = temp
        rear = temp
        return head, rear
     
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        
        head = None
        rear = None


        temp_list = []

        while(True):
            break_memory = True
            for i, temp_head in enumerate(lists):

                if(temp_head != None):
                    temp_list.append(temp_head.val)
                    lists[i] = temp_head.next
                    break_memory = False

            if(break_memory):
                break
            
        temp_list.sort()
        for element in temp_list:
            head, rear = self.insertAtEnd(head, rear, element)
        
        return head
    
l1 = ListNode(1, ListNode(4, ListNode(5)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
l3 = ListNode(2, ListNode(6))

lists = [l1, l2, l3]
solution = Solution()
result = solution.mergeKLists(lists)