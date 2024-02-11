class Solution:
    def minPartitions(self, n: str) -> int:
        
        return max([int(digit) for digit in n])

n = "32"
obj = Solution()
out = obj.minPartitions(n)
print(out)