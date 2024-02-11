class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        
        mat = [[0 for j in range(n)] for i in range(m)]
        
        for element in indices:

            i = 0
            while (i < n):
                
                mat[element[0]][i] += 1
                i += 1

            i = 0
            while (i < m):

                mat[i][element[1]] += 1
                i += 1

        count = 0
        i = 0
        while (i < m):
            
            j = 0
            while (j < n):

                if (mat[i][j] % 2 != 0):
                    count += 1

                j += 1
            
            i += 1

        return count
        

m = 2 
n = 2
indices = [[1,1],[0,0]]
obj = Solution()
solution = obj.oddCells(m, n, indices)
print(solution)