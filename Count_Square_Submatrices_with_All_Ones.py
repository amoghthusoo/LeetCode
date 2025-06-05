class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        
        dp_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        _sum = 0
        i = 0
        while(i < len(matrix)):

            j = 0
            while(j < len(matrix[0])):
                
                if(matrix[i][j]):
                    dp_matrix[i][j] = min(dp_matrix[i][j - 1], dp_matrix[i - 1][j - 1], dp_matrix[i - 1][j]) + 1
                
                _sum += dp_matrix[i][j]

                j += 1
            i += 1

        return _sum

matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
solution = Solution()
result = solution.countSquares(matrix)
print(result)