class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if(low == high):

            if(low % 2 == 0):
                return 0
            else:
                return 1
        
        if(low % 2 == 0):
            a = low + 1
        else:
            a = low

        if(high % 2 == 0):
            an = high - 1
        else:
            an = high

        return (an - a)//2 + 1