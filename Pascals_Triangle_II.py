from math import comb
class Solution:
    def generate(self, rowIndex: int) -> list:

        rowList = []

        j = 0
        while (j <= rowIndex):    
            rowList.append(comb(rowIndex, j))
            j += 1
            
        return rowList

rowIndex = 2
obj = Solution()
solution = obj.generate(rowIndex)
print(solution)