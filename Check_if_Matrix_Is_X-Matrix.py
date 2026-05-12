class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        
        i = 0
        while(i < len(grid)):

            if(grid[i][i] != 0):
                grid[i][i] = 0
            else:
                return False
            

            if(len(grid) % 2 != 0 and i == len(grid)//2):
                i += 1
                continue


            if(grid[i][len(grid) - 1 - i] != 0):
                grid[i][len(grid) - 1 - i] = 0
            else:
                return False

            i += 1
        
        i = 0
        while(i < len(grid)):
            
            j = 0
            while(j < len(grid[0])):

                if(grid[i][j] != 0):
                    return False

                j += 1
            i += 1

        return True

grid = [[5,0,20],[0,5,0],[6,0,2]]
obj = Solution()
result = obj.checkXMatrix(grid)
print(result)