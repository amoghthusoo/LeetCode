# NOT SOLVED
class Solution:
    def reverseBits(self, n: int) -> int:
        
        revStr : str = ""
        decNum : int = 0
        i = len(n) - 1
        while (i >= 0):
            revStr += n[i]
            i -= 1

        j = 0
        while (j < len(revStr)):

            decNum += int(revStr[j]) * 2 ** (len(revStr) - 1 - j)
            j += 1
        
        return decNum
        
        
n = "11111111111111111111111111111101"
obj = Solution()
solution = obj.reverseBits(n)
print(solution)