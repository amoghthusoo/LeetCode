class Solution:
    def maxProduct(self, n: int) -> int:
        
        n = sorted(list(str(n)), reverse = True)
        return int(n[0]) * int(n[1])

n = 22
obj = Solution()
result = obj.maxProduct(n)
print(result)

