class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row_indices = set()
        col_indices = set()

        i = 0
        while(i < len(matrix)):
            
            j = 0
            while(j < len(matrix[i])):

                if(matrix[i][j] == 0):
                    row_indices.add(i)
                    col_indices.add(j)

                j += 1
            i += 1

        while(len(row_indices) != 0):
            i = row_indices.pop()
            j = 0
            while(j < len(matrix[i])):
                matrix[i][j] = 0
                j += 1
        
        while(len(col_indices) != 0):   
            j = col_indices.pop()
            i = 0
            while(i < len(matrix)):
                matrix[i][j] = 0
                i += 1


matrix = [[1,1,1],[1,0,1],[1,1,1]]
solution = Solution()
result = solution.setZeroes(matrix)
print(result)
        
        