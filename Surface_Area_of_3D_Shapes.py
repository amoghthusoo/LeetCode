class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid)):

                if(j - 1 < 0):
                    ans += grid[i][j]
                else:

                    if(grid[i][j] > grid[i][j - 1]):
                        ans += grid[i][j] - grid[i][j - 1]
                

                if(i - 1 < 0):
                    ans += grid[i][j]
                else:

                    if(grid[i][j] > grid[i - 1][j]):
                        ans += grid[i][j] - grid[i - 1][j]
                

                if(j + 1 >= len(grid)):
                    ans += grid[i][j]
                
                else:

                    if(grid[i][j] > grid[i][j + 1]):
                        ans += grid[i][j] - grid[i][j + 1]
                

                if(i + 1 >= len(grid)):
                    ans += grid[i][j]
                
                else:

                    if(grid[i][j] > grid[i + 1][j]):
                        ans += grid[i][j] - grid[i + 1][j]
                

                if(grid[i][j] > 0):
                    ans += 2
        
        return ans

grid = [[2,2,2],[2,1,2],[2,2,2]]
obj = Solution()
result = obj.surfaceArea(grid)
print(result)