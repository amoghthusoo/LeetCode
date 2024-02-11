import sys
sys.set_int_max_str_digits(0)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        return str(int(num1) + int(num2))

num1 = "1"
num2 = "3"
obj = Solution()
solution = obj.addStrings(num1, num2)
print(solution)
