class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        
        start_color = (start[0] + start[1]) % 2
        target_color = (target[0] + target[1]) % 2

        if(start_color == target_color):
            return True
        else:
            return False