class Solution:
    def sumOfMultiples(self, n: int) -> int:
        
        _sum = 0

        for i in range(1, n + 1):

            if (i % 3 == 0 or i % 5 == 0 or i % 7 == 0):
                _sum += i

        return _sum

n = 9
obj = Solution()
solution = obj.sumOfMultiples(n)
print(solution)