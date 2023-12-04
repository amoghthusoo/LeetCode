class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def insertAtEnd(self, head, value):
        
        temp = ListNode()
        temp.val = value
        temp.next = None

        if(head == None):
            head = temp
        else:
            traversePtr = head
            
            while(traversePtr.next != None):
                traversePtr = traversePtr.next

            traversePtr.next = temp
        
        return head
    
    def linkedListToList(self, head):

        outList = []

        traversePtr = head
        while(traversePtr != None):
            
            outList.append(traversePtr.val)
            traversePtr = traversePtr.next
        
        return outList
    
    def listToLinkedList(self, inList):
        
        outHead = None

        for element in inList:
            outHead = self.insertAtEnd(outHead, element)

        return outHead
    
    def showLinkedList(self, head):

        while(head != None):
            print(f"{head.val} -> ", end="")
            head = head.next

        print(None)


class Solution:

    def listToNum(self, inList):
        
        outNum = ""

        for element in inList:
            outNum += str(element)

        return int(outNum)
    
    def numToList(self, num):

        outList = []
        
        for ch in str(num):
            outList.append(int(ch))

        return outList

    def addTwoNumbers(self, l1, l2):
        
        linkedListOperations = LinkedList()
        
        l1_list = linkedListOperations.linkedListToList(l1)
        l2_list = linkedListOperations.linkedListToList(l2)

        l1_list.reverse()
        l2_list.reverse()

        l1_num = self.listToNum(l1_list)
        l2_num = self.listToNum(l2_list)

        l3_num = l1_num + l2_num

        l3_list = self.numToList(l3_num)
        l3_list.reverse()

        l3 = linkedListOperations.listToLinkedList(l3_list)

        return l3

l1 = [2,4,3]
l2 = [5,6,4]
linkedListOperations = LinkedList()
l1_head = linkedListOperations.listToLinkedList(l1)
l2_head = linkedListOperations.listToLinkedList(l2)

obj = Solution()
outHead = obj.addTwoNumbers(l1_head, l2_head)
outList = linkedListOperations.showLinkedList(outHead)