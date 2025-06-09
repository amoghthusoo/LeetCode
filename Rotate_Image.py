class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        i = 0
        while(i < len(matrix)):
            j = 0
            while(j < len(matrix)):
                
                if(i > j):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                        
                j += 1
            i += 1

        
        i = 0
        while(i < len(matrix)):
            j = 0
            while(j < len(matrix)//2):

                matrix[i][j], matrix[i][len(matrix) - j - 1] = matrix[i][len(matrix) - j - 1], matrix[i][j]

                j += 1
            i += 1

        
matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution = Solution()
solution.rotate(matrix)
print(matrix)