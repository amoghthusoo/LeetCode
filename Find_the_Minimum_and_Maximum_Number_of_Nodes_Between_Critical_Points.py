# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> list[int]:
        
        node_list = []
        
        ptr = head
        while(ptr != None):
            node_list.append(ptr.val)
            ptr = ptr.next


        if(len(node_list) <= 3):
            return [-1, -1]
        
        critical_points = []
        i = 1
        while(i < len(node_list) - 1):

            if  (
                (node_list[i - 1] < node_list[i] and node_list[i + 1] < node_list[i]) or
                (node_list[i - 1] > node_list[i] and node_list[i + 1] > node_list[i])
                ):
                critical_points.append(i)

            i += 1

        if(len(critical_points) <= 1):
            return [-1, -1]
        
        max_dist = critical_points[-1] - critical_points[0]

        min_dist = critical_points[1] - critical_points[0]

        i = 1
        while(i < len(critical_points)):
            
            dist = critical_points[i] - critical_points[i - 1]
            if(dist < min_dist):
                min_dist = dist                
            i += 1

        return [min_dist, max_dist]
        