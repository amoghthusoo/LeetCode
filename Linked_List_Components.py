# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: ListNode, nums: list[int]) -> int:
        
        nums = set(nums)

        component = False
        count = 0
        ptr = head
        while(ptr != None):
            if(not component and ptr.val in nums):
                component = True
            
            if(component and ptr.val not in nums):
                component = False
                count += 1

            ptr = ptr.next
        
        if(component):
            count += 1

        return count