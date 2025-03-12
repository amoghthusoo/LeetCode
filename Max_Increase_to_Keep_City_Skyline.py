class Solution:

    def max_of_col(self, grid, j):

        _max = -1

        for i in range(len(grid)):
            if(grid[i][j] > _max):
                _max = grid[i][j]

        return _max

    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count += min(max(grid[i]), self.max_of_col(grid, j)) - grid[i][j]

        return count
    
grid = [[0,0,0],[0,0,0],[0,0,0]]
obj = Solution()
out = obj.maxIncreaseKeepingSkyline(grid)
print(out)