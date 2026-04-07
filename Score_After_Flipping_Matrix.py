class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        
        i = 0
        while(i < len(grid)):
            
            if(grid[i][0] == 0):
                j = 0
                while(j < len(grid[i])):
                    grid[i][j] ^= 1
                    j += 1
            i += 1

        j = 0
        while(j < len(grid[0])):

            zero_count = 0
            i = 0
            while(i < len(grid)):

                if(grid[i][j] == 0):
                    zero_count += 1
                i += 1

            if(zero_count > len(grid) - zero_count):
                i = 0
                while(i < len(grid)):
                    grid[i][j] ^= 1
                    i += 1
            j += 1

        _sum = 0
        for row in grid:
            bin_str = ""
            for digit in row:
                bin_str += str(digit)
            _sum += int(bin_str, 2)

        return _sum


grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
solution = Solution()
result = solution.matrixScore(grid)
print(result)