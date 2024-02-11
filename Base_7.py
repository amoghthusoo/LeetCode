class Solution:
    def convertToBase7(self, num: int) -> str:
        
        interStr = ""
        outStr = ""

        if (num >= 0):
            temp = num
        else:
            temp = -num

        while (temp != 0):
            interStr += str(temp % 7)
            temp //= 7

        i = len(interStr) - 1
        while (i >= 0):
            
            outStr += interStr[i]
            i -= 1
        

        if (num > 0):
            return outStr
        elif (num < 0):
            return "-" + outStr
        else:
            return "0"


num = 0
obj = Solution()
solution = obj.convertToBase7(num)
print(solution)
