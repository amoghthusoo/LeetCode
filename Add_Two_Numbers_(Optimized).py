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
    
    def linkedListToNum(self, head):
        
        traversePtr = head
        num_str = ""
        while(traversePtr != None):
            num_str += str(traversePtr.val)
            traversePtr = traversePtr.next
    
        return num_str
        
    def numToLinkedList(self, num):

        outHead = None

        for digit in num:
            outHead = self.insertAtEnd(outHead, int(digit))

        return outHead
        

class Solution:

    def reverseNum(self, num):

        outNum = ""
        i = len(num) - 1
        while(i >= 0):

            outNum += num[i]           
            i -= 1

        return outNum

    def addTwoNumbers(self, l1, l2):
        
        linkedListOperations = LinkedList()
        
        l1_num = linkedListOperations.linkedListToNum(l1)
        l2_num = linkedListOperations.linkedListToNum(l2)
        l1_num = self.reverseNum(l1_num)
        l2_num = self.reverseNum(l2_num)
        l3_num = int(l1_num) + int(l2_num)
        l3_num = self.reverseNum(str(l3_num))
        l3 = linkedListOperations.numToLinkedList(l3_num)

        return l3

l1 = [5,6]
l2 = [5,4,9]
linkedListOperations = LinkedList()
l1_head = linkedListOperations.listToLinkedList(l1)
l2_head = linkedListOperations.listToLinkedList(l2)

obj = Solution()
outHead = obj.addTwoNumbers(l1_head, l2_head)
outList = linkedListOperations.showLinkedList(outHead)