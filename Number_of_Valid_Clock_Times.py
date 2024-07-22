class Solution:
    def countTime(self, time: str) -> int:

        h1 = time[0]
        h2 = time[1]
        m1 = time[3]
        m2 = time[4]

        combinations = 1

        if(m2 == '?'):
            combinations *= 10
        
        if(m1 == '?'):
            combinations *= 6
        
        if(h1 != '?' and h2 == '?'):

            if(int(h1) <= 1):
                combinations *= 10
            else:
                combinations *= 4
        
        elif(h2 != '?' and h1 == '?'):
            
            if(int(h2) <= 3):
                combinations *= 3
            else:
                combinations *= 2

        elif(h1 == '?' and h2 == '?'):
            combinations *= 24

        return combinations