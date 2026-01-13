class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        

        i = len(colors) - 1
        while(i >= 0):

            if(colors[i] != colors[0]):
                break

            i -= 1
        
        d1 = i 

        i = 0
        while(i < len(colors)):

            if(colors[i] != colors[-1]):
                break

            i += 1
        
        d2 = len(colors) - 1 - i

        return max(d1, d2)
    