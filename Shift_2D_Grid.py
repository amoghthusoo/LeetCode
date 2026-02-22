class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:

        linear_arr = []
        
        for row in grid:
            for e in row:
                linear_arr.append(e)
        
        k = k % len(linear_arr)
        p1 = linear_arr[0 : len(linear_arr) - k]
        p2 = linear_arr[len(linear_arr) - k : ]

        linear_arr = p2 + p1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = linear_arr.pop(0)
        
        return grid