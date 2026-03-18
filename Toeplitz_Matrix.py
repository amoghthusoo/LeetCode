class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                
                x = i - 1
                y = j - 1

                if(x < 0 or y < 0):
                    continue

                if(matrix[i][j] != matrix[x][y]):
                    return False

        return True
