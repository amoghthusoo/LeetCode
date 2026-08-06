class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = None
        self.zero_cnt = 0
        self.ans = 0 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 0):
                    self.zero_cnt += 1
                elif(grid[i][j] == 1):
                    start = (i, j)
         
        def backtrack(grid, i, j, cnt):
             
            if(i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])):
                 return 
             
            elif(grid[i][j] == -1 or grid[i][j] == -2):
                 return
                 
            elif(grid[i][j] == 2):
                if(cnt == self.zero_cnt + 1):
                    self.ans += 1
                return
             
            grid[i][j] = -2
             
            backtrack(grid, i, j - 1, cnt + 1)
            backtrack(grid, i - 1, j, cnt + 1)
            backtrack(grid, i, j + 1, cnt + 1)
            backtrack(grid, i + 1, j, cnt + 1)
            grid[i][j] = 0
    
        backtrack(grid, start[0], start[1], 0)
        return self.ans 
             