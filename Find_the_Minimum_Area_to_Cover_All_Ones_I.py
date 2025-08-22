class Solution:
    def minimumArea(self, grid: list[list[int]]) -> int:
        
        min_i = 1000
        min_j = 1000
        max_i = -1
        max_j = -1

        i = 0
        while(i < len(grid)):
            j = 0
            while(j < len(grid[0])):

                if(grid[i][j] == 1):

                    if(i < min_i):
                        min_i = i

                    if(i > max_i):
                        max_i = i

                    if(j < min_j):
                        min_j = j

                    if(j > max_j):
                        max_j = j

                j += 1
            i += 1

        
        length = max_j - min_j + 1
        breadth = max_i - min_i + 1

        return length * breadth
    
grid = [[1,0],[0,0]]
obj = Solution()
result = obj.minimumArea(grid)
print(result)