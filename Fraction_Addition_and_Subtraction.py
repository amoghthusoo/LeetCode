from fractions import Fraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        fp = eval(expression)
        frac = Fraction(fp).limit_denominator()
        return f"{frac.numerator}/{frac.denominator}"
    
expression = "3"
obj = Solution()
result = obj.fractionAddition(expression)
print(result)

