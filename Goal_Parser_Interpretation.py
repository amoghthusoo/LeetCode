class Solution:
    def interpret(self, command: str) -> str:
        
        outStr = ""

        i = 0
        while (i < len(command)):

            if (command[i].isalpha()):
                outStr += command[i]
            elif (command[i] == '(' and command[i + 1] == ')'):
                outStr += 'o'

            i += 1

        return outStr

command = "(al)G(al)()()G"
obj = Solution()
solution = obj.interpret(command)
print(solution)