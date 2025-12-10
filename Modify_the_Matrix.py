class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        
        max_arr = []

        for j in range(len(matrix[0])):
            _max = -2
            for i in range(len(matrix)):
                if(matrix[i][j] > _max):
                    _max = matrix[i][j]
            
            max_arr.append(_max)

        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                if(matrix[i][j] == -1):
                    matrix[i][j] = max_arr[j]

        return matrix

matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
obj = Solution()
result = obj.modifiedMatrix(matrix)
print(result)