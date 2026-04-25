from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: ListNode) -> list[int]:

        node_list = []

        ptr = head
        while(ptr != None):
            node_list.append(ptr.val)
            ptr = ptr.next        

        stack = deque()
        ans = [None for _ in range(len(node_list))]

        for i, e in enumerate(node_list):

            if(len(stack) == 0 or e <= stack[-1][0]):
                stack.append((e, i))
            
            else:
                while(len(stack) != 0 and e > stack[-1][0]):
                    temp = stack.pop()
                    ans[temp[1]] = e
                stack.append((e, i))
        
        while(len(stack) != 0):
            temp = stack.pop()
            ans[temp[1]] = 0
        
        return ans

head = ListNode(2, ListNode(7, ListNode(4, ListNode(3, ListNode(5)))))
obj = Solution()
result = obj.nextLargerNodes(head)
print(result)
