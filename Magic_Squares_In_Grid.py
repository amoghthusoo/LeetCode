class Solution:

    def __init__(self):
        self.num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def is_magic_square(self, grid, x, y):

        _1 = grid[x][y]
        _2 = grid[x][y + 1]
        _3 = grid[x][y + 2]
        
        _4 = grid[x + 1][y]
        _5 = grid[x + 1][y + 1]
        _6 = grid[x + 1][y + 2]
        
        _7 = grid[x + 2][y]
        _8 = grid[x + 2][y + 1]
        _9 = grid[x + 2][y + 2]

        if({_1, _2, _3, _4, _5, _6, _7, _8, _9} == self.num_set):
            if((_1 + _2 + _3) == (_4 + _5 + _6) == (_7 + _8 + _9) == (_1 + _4 + _7) == (_2 + _5 + _8) == (_3 + _6 + _9) == (_1 + _5 + _9) == (_3 + _5 + _7)):
                return True
        
        return False

    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        
        ans = 0
        i = 0
        while(i <= len(grid) - 3):
            
            j = 0
            while(j <= len(grid[0]) - 3):
                
                if(self.is_magic_square(grid, i, j)):
                    ans += 1

                j += 1
            i += 1
        
        return ans 

grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
obj = Solution()
result = obj.numMagicSquaresInside(grid)
print(result)