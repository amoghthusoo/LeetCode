from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0    
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 2):
                    queue.append((i, j))
        
        while(queue):
        
            n = len(queue)
            time_flag = False
            
            for _ in range(n):

                i, j = queue.popleft()
                grid[i][j] = 2

                if(j - 1 >= 0 and grid[i][j - 1] == 1):
                    grid[i][j - 1] = 2
                    queue.append((i, j - 1))
                    time_flag = True
                if(i - 1 >= 0 and grid[i - 1][j] == 1):
                    grid[i - 1][j] = 2
                    queue.append((i - 1, j))
                    time_flag = True
                if(j + 1 < len(grid[0]) and grid[i][j + 1] == 1):
                    grid[i][j + 1] = 2
                    queue.append((i, j + 1))
                    time_flag = True
                if(i + 1 < len(grid) and grid[i + 1][j] == 1):
                    grid[i + 1][j] = 2
                    queue.append((i + 1, j))
                    time_flag = True
            
            if(time_flag): 
                time += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    return -1
        return time