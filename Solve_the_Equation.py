class Solution:

    def simplify(self, eq):
        
        x_count = 0
        while("x" in eq):

            index = eq.index("x")

            if(index == 0):
                x_count += 1
                eq.pop(0)

            elif(index == 1):
        
                if(eq[0].isdigit()):
                    coff = int(eq[0])
                    x_count += coff

                else:

                    if(eq[0] == "+"):
                        x_count += 1
                    else:
                        x_count -= 1

                eq.pop(0)
                eq.pop(0)
            
            else:

                if(eq[index - 1].isdigit()):
                    coff = int(eq[index - 1])
                    
                    if(eq[index - 2] == "+"):
                        x_count += coff
                    else:
                        x_count -= coff
                    
                    eq.pop(index - 2)
                    eq.pop(index - 2)
                    eq.pop(index - 2)
                
                else:

                    if(eq[index - 1] == "+"):
                        x_count += 1
                    else:
                        x_count -= 1

                    eq.pop(index - 1)
                    eq.pop(index - 1)
            
        return x_count
    
    def tokenize(self, eq):
        
        eq_arr = []

        num = ""
        i = 0
        while(i < len(eq)):
            
            if(eq[i] in ["+", "-", "x"]):

                if(num):
                    eq_arr.append(num)
                    num = ""

                eq_arr.append(eq[i])
            
            else:
                num += eq[i]

            i += 1

        if(num):
            eq_arr.append(num)
        
        return eq_arr

    def solveEquation(self, equation: str) -> str:
        
        equation = equation.split("=")

        LHS = self.tokenize(equation[0])
        RHS = self.tokenize(equation[1])

        lhs_x_count = self.simplify(LHS)
        rhs_x_count = self.simplify(RHS)

        lhs_expr = "".join(LHS)
        rhs_expr = "".join(RHS)

        if(lhs_expr):
            lhs_expr = eval(lhs_expr)
        else:
            lhs_expr = 0
        
        if(rhs_expr):
            rhs_expr = eval(rhs_expr)
        else:
            rhs_expr = 0
        
        numerator = rhs_expr - lhs_expr
        denominator = lhs_x_count - rhs_x_count

        if(numerator == denominator == 0):
            return "Infinite solutions"
        elif(denominator == 0):
            return "No solution"
        else:
            ans = numerator // denominator
            return f"x={ans}"
                

equation = "99x=99"
obj = Solution()
result = obj.solveEquation(equation)
print(result)
        
            


