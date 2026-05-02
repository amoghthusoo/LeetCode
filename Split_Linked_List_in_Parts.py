# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> list[ListNode]:
        
        node_list = []

        traversePtr = head
        while(traversePtr != None):
            node_list.append(traversePtr)
            traversePtr = traversePtr.next
        
        ans = []
        if(len(node_list) <= k):
            
            for e in node_list:
                e.next = None
                ans.append(e)

            for _ in range(k - len(node_list)):
                ans.append(None)

        elif(len(node_list) % k == 0):

            i = 0
            while(i  < len(node_list)):
                ans.append(node_list[i])
                i += len(node_list) // k

                node_list[i - 1].next = None

            # for i in range(0, len(node_list), len(node_list) // k):
            #     ans.append(node_list[i])
        
        else:
            
            extra_elements = len(node_list) % k

            i = 0
            for _ in range(extra_elements):
                ans.append(node_list[i])
                i += len(node_list) // k + 1
                node_list[i - 1].next = None

            for _ in range(k - extra_elements):
                ans.append(node_list[i])
                i += len(node_list) // k
                node_list[i - 1].next = None

        return ans