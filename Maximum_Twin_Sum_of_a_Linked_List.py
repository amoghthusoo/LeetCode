# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: ListNode) -> int:
        
        node_values = []

        traversePtr = head
        while(traversePtr != None):

            node_values.append(traversePtr.val)
            traversePtr = traversePtr.next

        max_sum = -int(2 ** 31)

        i = 0
        j = -1

        while(i < len(node_values)):

            temp_sum = node_values[i] + node_values[j]

            if(temp_sum > max_sum):
                max_sum = temp_sum

            i += 1
            j -= 1

        return max_sum