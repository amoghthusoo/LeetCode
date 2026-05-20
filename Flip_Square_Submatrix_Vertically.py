class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        
        for j in range(k):
            for i in range(k // 2):

                grid[x + i][y + j], grid[x + k - i - 1][j + y] = grid[x + k - i - 1][j + y], grid[x + i][y + j]
        
        return grid

grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
x = 1
y = 0
k = 3

obj = Solution()
result = obj.reverseSubmatrix(grid, x, y, k)
print(result)