class Solution:
    def decimalRepresentation(self, n: int) -> list[int]:
        
        n = str(n)

        ans = []
        for i, e in enumerate(n):

            if(e != "0"):
                ans.append(int(e) * int(10 ** (len(n) - 1 - i)))
        
        return ans
