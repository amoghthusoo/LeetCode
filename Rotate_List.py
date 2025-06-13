# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if(k == 0):
            return head
        
        elif(head == None):
            return head

        tail = None
        n = 0
        traversePtr = head
        while(traversePtr != None):
            n += 1
            if(traversePtr.next == None):
                tail = traversePtr
            traversePtr = traversePtr.next

        k %= n 

        traversePtr = head
        i = 1
        while(i < n - k):

            traversePtr = traversePtr.next
            i += 1

        tail.next = head
        head = traversePtr.next
        traversePtr.next = None

        return head

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2
solution = Solution()
result = solution.rotateRight(head, k)
print(result)