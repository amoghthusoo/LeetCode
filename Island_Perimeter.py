class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:

        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if(grid[i][j] == 1):

                    count = 0

                    
                    if(j - 1 >= 0):
                        if(grid[i][j - 1] == 1):
                            count += 1
                    
                    if(i - 1 >= 0):
                        if(grid[i - 1][j] == 1):
                            count += 1
                    
                    try:
                        if(grid[i][j + 1] == 1):
                            count += 1
                    except:
                        pass
                    try:
                        if(grid[i + 1][j] == 1):
                            count += 1
                    except:
                        pass
                    
                    perimeter += 4 - count

        return perimeter

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
obj = Solution()
out = obj.islandPerimeter(grid)
print(out)
