from math import comb
class Solution:
    def generate(self, numRows: int) -> list:

        numRows -= 1
        pascalsTriangle = []

        i = 0
        while (i <= numRows):
            rowList = []
            
            j = 0
            while (j <= i):    
                rowList.append(comb(i, j))
                j += 1
            
            pascalsTriangle.append(rowList)
            i += 1 

        return pascalsTriangle

numRows = 10
obj = Solution()
solution = obj.generate(numRows)
print(solution)