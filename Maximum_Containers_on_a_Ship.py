class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        
        p = n * n * w 
        if(p <= maxWeight):
            return n * n 
        else:
            return maxWeight // w 