class Solution:
    def satisfiesConditions(self, grid: list[list[int]]) -> bool:
        
        i = 0
        while(i < len(grid) - 1):

            j = 0
            while(j < len(grid[0])):

                if(grid[i][j] == grid[i + 1][j]):
                    pass
                else:
                    return False

                j += 1
            i += 1

        i = 0
        while(i < len(grid)):

            j = 0
            while(j < len(grid[0]) - 1):

                if(grid[i][j] != grid[i][j + 1]):
                    pass
                    
                else:
                    return False


                j +=1
            i +=1

        return True