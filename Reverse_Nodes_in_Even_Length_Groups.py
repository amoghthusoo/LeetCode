# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, node_list):

        i = len(node_list) - 1
        while(i > 0):
            node_list[i].next = node_list[i - 1]
            i -= 1
        node_list[0].next = None

    def reverseEvenLengthGroups(self, head: ListNode) -> ListNode:
        
        node_list = []

        group_size = 1
        count = 0
        temp =[]
        ptr = head
        while(ptr != None):
            
            if(count != group_size):
                temp.append(ptr)
                count += 1
            else:
                node_list.append(temp)
                temp = []
                temp.append(ptr)
                group_size += 1
                count = 1

            ptr = ptr.next
        node_list.append(temp)

        i = 1
        while(i < len(node_list) - 1):

            self.reverseList(node_list[i])
            node_list[i - 1][-1].next = node_list[i][-1]
            try:
                node_list[i][0].next = node_list[i + 1][0]
            except:
                pass

            i += 2

        if(len(node_list[-1]) % 2 == 0):
            self.reverseList(node_list[-1])
            
            if(len(node_list[-2]) % 2 == 0):
                node_list[-2][0].next = node_list[-1][-1]
            else:
                node_list[-2][-1].next = node_list[-1][-1]

        return head
        
head = ListNode(5, ListNode(2, ListNode(3, ListNode(4, ListNode(8)))))
obj = Solution()
result = obj.reverseEvenLengthGroups(head)
