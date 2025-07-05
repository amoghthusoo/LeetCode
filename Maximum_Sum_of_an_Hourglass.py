class Solution:
    def maxSum(self, grid: list[list[int]]) -> int:
        
        max_sum = -1

        i = 0
        while(i < len(grid)):
            
            j = 0
            while(j < len(grid[0])):

                try:
                    temp_sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                    if(temp_sum > max_sum):
                        max_sum = temp_sum
                except:
                    break

                j += 1            
            i += 1

        return max_sum