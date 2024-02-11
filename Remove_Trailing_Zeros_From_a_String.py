class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        
        return num.rstrip('0')

num = "123"
obj = Solution()
solution = obj.removeTrailingZeros(num)
print(solution)