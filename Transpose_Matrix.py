class Solution:
    def transpose(self, matrix: list) -> list:
        
        rows1 = len(matrix)
        columns1 = len(matrix[0])

        rows2 = columns1
        columns2 = rows1

        transMatrix = []
        for i in range(rows2):
            transMatrix.append([None for i in range(columns2)])

        
        i = 0
        while (i < rows1):
            j = 0
            while (j < columns1):

                transMatrix[j][i] = matrix[i][j] 
                j += 1
            
            i += 1

        return transMatrix


matrix = [[1,2,3],[4,5,6]]
obj = Solution()
solution = obj.transpose(matrix)
print(solution)