class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        
        _sum = 0

        for i in range(len(grid)):
            for j in range(len(grid)):
                if(grid[i][j] != 0):
                    _sum += 1

        for i in range(len(grid)):
            _sum += max(grid[i])

        for j in range(len(grid)):
            _max = -1
            for i in range(len(grid)):
                if(grid[i][j] > _max):
                    _max = grid[i][j]
            
            _sum += _max
        
        return _sum