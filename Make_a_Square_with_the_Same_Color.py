class Solution:
    def canMakeSquare(self, grid: list[list[str]]) -> bool:
        
        mat = [grid[0][0], grid[0][1], grid[1][0], grid[1][1]]
        
        if(mat.count("B") >= 3 or mat.count("W") >= 3):
            return True
        
        mat = [grid[0][1], grid[0][2], grid[1][1], grid[1][2]]
        if(mat.count("B") >= 3 or mat.count("W") >= 3):
            return True
        
        mat = [grid[1][0], grid[1][1], grid[2][0], grid[2][1]]
        if(mat.count("B") >= 3 or mat.count("W") >= 3):
            return True
        
        mat = [grid[1][1], grid[1][2], grid[2][1], grid[2][2]]
        if(mat.count("B") >= 3 or mat.count("W") >= 3):
            return True
        
        return False