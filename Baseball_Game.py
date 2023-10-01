class Solution:
    def calPoints(self, operations: list[str]) -> int:
        
        interList = list()

        for element in operations:

            if (element == '+'):
                interList.append(interList[-1] + interList[-2])
            elif(element == 'D'):
                interList.append(interList[-1] * 2)
            elif (element == 'C'):
                interList.pop()
            else:
                interList.append(int(element))

        return sum(interList)

operations = ["1","C"]
obj = Solution()
solution = obj.calPoints(operations)
print(solution)