class Solution:
    def sumAndMultiply(self, n: int) -> int:
        
        intr = ""
        n = str(n)
        for ch in n:
            if(ch != "0"):
                intr += ch
        
        if(intr):
            _total = 0
            for digit in intr:
                _total += int(digit)
            
            return int(intr) * _total
        
        return 0
        
