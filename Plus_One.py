class Solution:
    def plusOne(self, digits: list) -> list:

        digitsStr = ""
        outList = []
        for element in digits:
            digitsStr += str(element)

        digitsStr = str(int(digitsStr) + 1)

        for element in digitsStr:
            outList.append(int(element))
        
        return outList

digits = [9]
obj = Solution()
solution = obj.plusOne(digits)
print(solution)