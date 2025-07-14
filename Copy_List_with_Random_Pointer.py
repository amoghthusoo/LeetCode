# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def insertAtEnd(self, head, rear, val):

        temp = Node(val)
        
        if(head == rear == None):    
            head = rear = temp
            return head, rear, temp
        
        rear.next = temp
        rear = temp

        return head, rear, temp
    
    def copyRandomList(self, head: Node) -> Node:
        
        state_dict = {}
        node_list = []
        copy_node_list = []

        copy_head = copy_rear = None

        i = 0
        ptr = head
        while(ptr != None):
            
            state_dict[ptr] = i
            node_list.append(ptr)
            copy_head, copy_rear, temp = self.insertAtEnd(copy_head, copy_rear, ptr.val)
            copy_node_list.append(temp) 

            i += 1
            ptr = ptr.next

        
        for i, node in enumerate(node_list):
            
            rand_ptr = node.random
            
            if(rand_ptr != None):
                rand_index = state_dict[rand_ptr]
                copy_node_list[i].random = copy_node_list[rand_index]
            else:
                copy_node_list[i].random = None

        return copy_head    
