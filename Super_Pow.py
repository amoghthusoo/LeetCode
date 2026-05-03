class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        
        p = ""
        for e in b:
            p += str(e)
        p = int(p)

        return pow(a, p, 1337)