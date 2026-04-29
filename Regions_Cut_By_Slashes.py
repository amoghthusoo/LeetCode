class Solution:

    def __init__(self):
        self.pixel_grid = []
        self.visited = set()

    def get_exit_points(self, i, j):
        
        exit_points = []
        
        if((i - 1, j) not in self.visited and i - 1 >= 0 and self.pixel_grid[i - 1][j] != 1):
            exit_points.append((i - 1, j))
        
        if((i, j - 1) not in self.visited and j - 1 >= 0 and self.pixel_grid[i][j - 1] != 1):
            exit_points.append((i, j - 1))
        
        if((i, j + 1) not in self.visited and j + 1 < len(self.pixel_grid) and self.pixel_grid[i][j + 1] != 1):
            exit_points.append((i, j + 1))
        
        if((i + 1, j) not in self.visited and i + 1 < len(self.pixel_grid) and self.pixel_grid[i + 1][j] != 1):
            exit_points.append((i + 1, j))
        
        return exit_points
    
    def identify_component(self) -> bool:
        
        break_mem = False
        for i in range(len(self.pixel_grid)):
            for j in range(len(self.pixel_grid)):
                if(self.pixel_grid[i][j] != 1 and (i, j) not in self.visited):
                    break_mem = True
                    break
            if(break_mem):
                break
        
        if(not break_mem):
            return False
        
        stack = []
    
        while(True):
            
            self.visited.add((i, j))
            
            exit_points = self.get_exit_points(i, j)

            if(len(exit_points) == 0):
                try:
                    checkpoint = stack.pop()
                except:
                    return True
                
                i = checkpoint[0]
                j = checkpoint[1]
                continue

            elif(len(exit_points) != 1):
                stack.append((i, j))
            
            i = exit_points[0][0]
            j = exit_points[0][1]

    def regionsBySlashes(self, grid: list[str]) -> int:

        self.pixel_grid = [[0 for _ in range(len(grid) * 3)] for _ in range(len(grid) * 3)]

        i = 0
        j = 0
        for row in grid:
            for e in row:
                if(e == " "):
                    pass
                elif(e == "/"):
                    
                    self.pixel_grid[i][j] = 0
                    self.pixel_grid[i][j + 1] = 0
                    self.pixel_grid[i][j + 2] = 1
                    self.pixel_grid[i + 1][j] = 0
                    self.pixel_grid[i + 1][j + 1] = 1
                    self.pixel_grid[i + 1][j + 2] = 0
                    self.pixel_grid[i + 2][j] = 1
                    self.pixel_grid[i + 2][j + 1] = 0
                    self.pixel_grid[i + 2][j + 2] = 0
                else:
                    self.pixel_grid[i][j] = 1
                    self.pixel_grid[i][j + 1] = 0
                    self.pixel_grid[i][j + 2] = 0
                    self.pixel_grid[i + 1][j] = 0
                    self.pixel_grid[i + 1][j + 1] = 1
                    self.pixel_grid[i + 1][j + 2] = 0
                    self.pixel_grid[i + 2][j] = 0
                    self.pixel_grid[i + 2][j + 1] = 0
                    self.pixel_grid[i + 2][j + 2] = 1

                j = (j + 3) % len(self.pixel_grid)
            i += 3

        components = 0
        while(self.identify_component()):
            components += 1
        
        return components

grid = ["/\\","\\/"]
obj = Solution()
result = obj.regionsBySlashes(grid)
print(result)
