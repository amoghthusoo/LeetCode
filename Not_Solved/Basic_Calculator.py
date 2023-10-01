# NOT SOLVED
class Solution:
    def calculate(self, s: str) -> int:

        # <---------------------------------Implementation of Stacks starts here----------------------------------------->

        # push function for stack implementation
        def push(stack : list, element : str) -> None:
            
            stack.append(element)
            return None

        # pop function for stack implementation
        def pop(stack : list) -> str:
            
            if (len(stack) == 0):
                return None
            else:
                return stack.pop()
            
        # isEmpty function for stack implementation
        def isEmpty(stack : list) -> bool:
            
            if (len(stack) == 0):
                return True
            else:
                return False

        # top function for stack implementation
        def top(stack : list) -> None | str:
            
            if (isEmpty(stack)):
                return None
            else:
                return stack[-1]

        # size function for stack implementation
        def size(stack : list) -> int:
            return len(stack)

        # <---------------------------------Implementation of Stacks ends here----------------------------------------->

        # This returns the relative precedence of arithmetic operators
        def precedence(operator : str) -> int:

            if operator in ['(', ')']:
                return -1                                   # Do not confuse with the actual precedence of brackets. {Added during debugging process.}
            elif operator in ['+', '-']:
                return 0
            elif operator in ['*', '/']:
                return 1

        # This function returns whether the character is an operator or not    
        def isOperator(character : str) -> bool:
            
            if character in ['+', '-', '*', '/', '(', ')']:             # '(' and ')' are added to the list during debugging process.         
                return True
            else:
                return False

        # This function converts the input expression which is stored in a string into the list.
        """
        It is found that processing the input expression directly; only works with single digit numbers.
        After this conversion, processing the inExp works for double digts as well and so on.
        """ 
        def converterStringList(inStr : str) -> list:

            inExp : list = []
            inStr_index : int = 0
            inExp_index : int = 0
            unary_memory : bool = True                      # Counter for the total number of indices in "inExp" list.                                   
            while (inStr_index < len(inStr)):               #{Added during debugging, handles the case when expression starts with unary operator}
                if (not isOperator(inStr[inStr_index])):
                    
                    if (inStr_index == 0):
                        inExp.append(inStr[inStr_index])
                    
                    elif (inStr_index > 0) and (isOperator(inExp[0][0])) and (unary_memory): # {Added during debugging, handles the case when expression starts with unary operator}
                        inExp[inExp_index] += inStr[inStr_index]                                  # <--------------------------------------do------------------------------------------->

                    elif (isOperator(inExp[-1])):
                        inExp.append(inStr[inStr_index])
                        inExp_index += 1
                    
                    else:
                        inExp[inExp_index] += inStr[inStr_index]
                
                elif (isOperator(inStr[inStr_index])):
                    inExp.append(inStr[inStr_index])
                    
                    if (inStr_index != 0):      # {Added during debugging, handles the case when expression starts with unary operator}
                        inExp_index += 1

                    if (inExp_index == 1):      # {Added during debugging, handles the case when expression starts with unary operator}
                        unary_memory = False    # <--------------------------------------do------------------------------------------->
                    
                inStr_index += 1

            return inExp

        # This function converts the infix expression to postfix expression.
        def converterPostExp(inExp : list) -> list:

            postExp : list = []
            stack : list = []

            for ch in inExp:

                if ch == '(':
                    push(stack, ch)

                elif ch == ')':
                    
                    while True:
                        popped_character : str = pop(stack)
                        if popped_character == '(':
                            break
                        else:
                            postExp.append(popped_character)

                elif isOperator(ch):

                    if isEmpty(stack):
                        push(stack, ch)

                    elif (precedence(ch) <= precedence(top(stack))):            # Equality handles the associativity of operators from left to right

                        while (not isEmpty(stack)):

                            top_character : str = top(stack)

                            if (precedence(top_character) < precedence(ch)):
                                break
                            
                            else:
                                postExp += pop(stack)

                        stack.append(ch)                                    
                    
                    else:
                        push(stack, ch)
                
                else:
                    postExp.append(ch)
                
            while (not isEmpty(stack)):
                postExp += pop(stack)

            return postExp

        # This function evaluates the postfix expression.
        def evalMod(inStr : str) -> str:


            inExp = converterStringList(inStr)
            postExp = converterPostExp(inExp)
            
            stack : list = []
            for ch in postExp:
                if (not isOperator(ch)):
                    push(stack, ch)
                else:
                    element2 : str = pop(stack)
                    element1 : str = pop(stack)
                    if (ch == '+'):
                        intemediate_result : str = str(float(element1) + float(element2))
                    elif (ch == '-'):
                        intemediate_result : str = str(float(element1) - float(element2))
                    elif (ch == '*'):
                        intemediate_result : str = str(float(element1) * float(element2))
                    elif (ch == '/'):
                            intemediate_result : str = str(float(element1) / float(element2))  # Zero division exception can occur. {to be handled}        
                    push(stack, intemediate_result)

            
            result : str = pop(stack)     # Logical errors may arise in case of invalid input from the user.       
            return result
        
        
        return evalMod(s)



s = "(1+(4+5+2)-3)+(6+8)"
obj = Solution()
solution = obj.calculate(s)
print(solution)