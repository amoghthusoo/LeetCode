# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        
        reference_list = []

        traversePtr = head
        while(traversePtr != None):
            reference_list.append(traversePtr)
            traversePtr = traversePtr.next

        if(len(reference_list) == 0):
            return None
        elif(len(reference_list) == 1):
            return reference_list[0]

        i = 0
        while(i < len(reference_list)):

            try:
                reference_list[i + 1].next = reference_list[i]
                reference_list[i].next = reference_list[i + 3]

            except:
                if(len(reference_list) % 2 == 0):
                    reference_list[i].next = None
                else:
                    reference_list[i].next = reference_list[-1]

                break

            i += 2

        return reference_list[1]

n1 = None
# n2 = ListNode(2)
# n3 = ListNode(3)
# n4 = ListNode(4)
# n5 = ListNode(5)
# n6 = ListNode(6)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6

obj = Solution()
out = obj.swapPairs(n1)

while(out != None):
    print(out.val)
    out = out.next