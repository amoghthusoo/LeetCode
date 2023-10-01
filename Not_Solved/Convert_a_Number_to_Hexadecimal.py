# NOT SOLVED
class Solution:
    def toHex(self, num: int) -> str:
        
        return hex(num)[2:]


num = 26
obj = Solution()
solution = obj.toHex(num)
print(solution)