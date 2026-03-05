class Solution:
    def minOperations(self, s: str) -> int:
        
        c1 = 0
        for i, e in enumerate(s):
            if((i % 2 == 0 and e != "0") or (i % 2 != 0 and e != "1")):
                c1 += 1
        
        c2 = 0
        for i, e in enumerate(s):
            if((i % 2 == 0 and e != "1") or (i % 2 != 0 and e != "0")):
                c2 += 1

        return min(c1, c2)
