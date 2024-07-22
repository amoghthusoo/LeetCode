class Solution:
    
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        
        out_mat = [[None for _ in range(len(grid) - 2)] for _ in range(len(grid) - 2)]


        for i in range(len(out_mat)):
            for j in range(len(out_mat)):

                out_mat[i][j] = max([grid[i][j], grid[i][j + 1], grid[i][j + 2],
                                     grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2],
                                     grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]
                                     ])
                

        return out_mat

