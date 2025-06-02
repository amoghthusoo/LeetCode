class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        
        _sum = 0
        for digit in str(x):
            _sum += int(digit)
        
        if(x % _sum == 0):
            return _sum
        else:
            return -1
        
x = 18
solution = Solution()
result = solution.sumOfTheDigitsOfHarshadNumber(x)
print(x)