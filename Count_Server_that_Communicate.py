class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        
        row_map = dict()
        col_map = dict()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                e = grid[i][j]
                if(e == 1):
                    
                    if(i not in row_map):
                        row_map[i] = 1
                    else:
                        row_map[i] += 1

                    if(j not in col_map):
                        col_map[j] = 1
                    else:
                        col_map[j] += 1
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                e = grid[i][j]

                if(e == 1):

                    if(row_map[i] >= 2 or col_map[j] >= 2):
                        ans += 1
        
        return ans