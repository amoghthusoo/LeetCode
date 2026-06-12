from collections import Counter
class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        
        n = str(n)
        x = str(x)

        if(n[0] == x):
            return False
        
        occr_dict = Counter(n)

        if(occr_dict[x] >= 1):
            return True
        
        return False