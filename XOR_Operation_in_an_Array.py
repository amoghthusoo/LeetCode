class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        xor = 0
        
        i = 0
        while(i < n):
            xor ^= (start + (2 * i))
            i += 1

        return xor