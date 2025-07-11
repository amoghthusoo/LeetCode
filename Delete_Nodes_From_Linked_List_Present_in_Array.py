# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        
        nums = set(nums)

        node_list = []
        ptr = head
        while(ptr != None):
            node_list.append(ptr)
            ptr = ptr.next
        
        refined_list = []
        for i, e in enumerate(node_list):
            if(e.val not in nums):
                refined_list.append(e)
        
        i = 0
        while(i < len(refined_list) - 1):
            refined_list[i].next = refined_list[i + 1]
            i += 1

        refined_list[-1].next = None

        return refined_list[0]

nums = [1,2,3]
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
obj = Solution()
result = obj.modifiedList(nums, head)
print(result)
