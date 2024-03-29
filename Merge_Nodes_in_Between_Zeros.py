# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class AccessList:

    def __init__(self):
        self.head : ListNode = None
        self.rear : ListNode = None


class Solution:
    def insertAtEnd(self, accessList, val):
        
        temp = ListNode(val)
    
        if(accessList.head == None):
            accessList.head = temp
            accessList.rear = temp

        else:
            accessList.rear.next = temp
            accessList.rear = temp

        return accessList
    
    def mergeNodes(self, head: ListNode) -> ListNode:

        accessList = AccessList()
        total = 0

        traversePtr = head
        traversePtr = traversePtr.next

        while(traversePtr != None):

            if(traversePtr.val == 0):
                accessList = self.insertAtEnd(accessList, total)
                total = 0
            else:
                total += traversePtr.val

            traversePtr = traversePtr.next
        
        return accessList.head



# obj = Solution()
# out = obj.mergeNodes()
# print(out)