# NOT SOLVED
class Solution:
    def addTwoNumbers(self, l1: list, l2: list) -> list:

        def listToNum(_list : list) -> str:

            numStr = ""
            _list.reverse()
            for element in _list:
                numStr += str(element)
            
            return numStr
        
        num1Str : str = listToNum(l1)
        num2Str : str = listToNum(l2)
        numResultStr : str = str(int(num1Str) + int(num2Str))
        outList : list = []

        i = len(numResultStr) - 1
        while (i >= 0):
            outList.append(int(numResultStr[i]))
            i -= 1
        
        return outList


l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
obj = Solution()
solution = obj.addTwoNumbers(l1, l2)
print(solution)