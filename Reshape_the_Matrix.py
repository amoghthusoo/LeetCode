class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:

        if(r * c != len(mat) * len(mat[0])):
            return mat
        
        out_matrix = [[None for _ in range(c)] for _ in range(r)]

        x = 0
        y = 0

        i = 0
        while(i < r):
            
            j = 0
            while(j < c):

                
                out_matrix[i][j] = mat[x][y]
                

                if(y == len(mat[0]) - 1):
                    x += 1
                    y = 0
                else:
                    y += 1

                j += 1
            i += 1

        return out_matrix
    
mat = [[1,2]]
r = 1
c = 1

obj = Solution()
out = obj.matrixReshape(mat, r, c)
print(out)