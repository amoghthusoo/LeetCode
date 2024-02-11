class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        _sum = 0
        product = 1

        for digit in str(n):
            _sum += int(digit)
            product *= int(digit)

        return product - _sum



n = 4421
obj = Solution()
solution = obj.subtractProductAndSum(n)
print(solution)
