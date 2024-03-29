class Solution:

    def isMaxInColumn(self, matrix, num, column) -> bool:

        j = column
        i = 0
        while(i < len(matrix)):
            
            if(matrix[i][column] > num):
                return False
            i += 1

        return True 

    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
        
        outArr = []

        i = 0
        while(i < len(matrix)):

            minElement = min(matrix[i])

            if(self.isMaxInColumn(matrix, minElement, matrix[i].index(minElement))):
                outArr.append(minElement)


            i += 1

        return outArr



matrix = [[7,8],[1,2]]
obj = Solution()
out = obj.luckyNumbers(matrix)
print(out)