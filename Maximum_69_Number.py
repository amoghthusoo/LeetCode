class Solution:
    def maximum69Number (self, num: int) -> int:
        
        interList = list(str(num))

        i = 0
        while (i < len(interList)):
            
            if (interList[i] == '6'):
                interList[i] = '9'
                break

            i += 1

        interStr = ""

        for element in interList:
            interStr += element

        return int(interStr)
            
num = 9999
obj = Solution()
solution = obj.maximum69Number(num)
print(solution)