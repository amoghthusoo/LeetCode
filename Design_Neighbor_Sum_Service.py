class NeighborSum:

    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        

    def getIndex(self, target):

        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if(self.grid[i][j] == target):
                    return i, j
                
    def adjacentSum(self, value: int) -> int:
        
        i, j = self.getIndex(value)
        total = 0

        if(j - 1 >= 0):
            total += self.grid[i][j - 1]

        if(i - 1 >= 0):
            total += self.grid[i - 1][j]

        try:
            total += self.grid[i][j + 1]
        except:
            pass

        try:
            total += self.grid[i + 1][j]
        except:
            pass

        return total

    def diagonalSum(self, value: int) -> int:

        i, j = self.getIndex(value)
        total = 0

        if(i - 1 >= 0 and j - 1 >= 0):
            total += self.grid[i - 1][j - 1]

        if(i - 1 >= 0):
            try:
                total += self.grid[i - 1][j + 1]
            except:
                pass

        if(j - 1 >= 0):
            try:
                total += self.grid[i + 1][j - 1]
            except:
                pass

        try:
            total += self.grid[i + 1][j + 1]
        except:
            pass

        return total

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)