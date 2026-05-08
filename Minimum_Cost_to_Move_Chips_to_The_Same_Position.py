class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:

        even = 0
        for e in position:
            if(e % 2 == 0):
                even += 1
        odd = len(position) - even 

        return min(even, odd)
