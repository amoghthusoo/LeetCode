class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        
        grid = [[None for _ in range(n)] for _ in range(m)]

        for guard in guards:
            grid[guard[0]][guard[1]] = "g"
        
        for wall in walls:
            grid[wall[0]][wall[1]] = "w"

        for guard in guards:

            # left
            i = guard[0]
            j = guard[1] - 1
            while(j >= 0 and grid[i][j] not in ["g", "w"]):
                grid[i][j] = True
                j -= 1
            
            # up
            i = guard[0] - 1
            j = guard[1]
            while(i >= 0 and grid[i][j] not in ["g", "w"]):
                grid[i][j] = True
                i -= 1
            
            # right
            i = guard[0]
            j = guard[1] + 1
            while(j < n and grid[i][j] not in ["g", "w"]):
                grid[i][j] = True
                j += 1
            
            # down
            i = guard[0] + 1
            j = guard[1]
            while(i < m and grid[i][j] not in ["g", "w"]):
                grid[i][j] = True
                i += 1
        
        ans = 0
        for row in grid:
            ans += row.count(None)
        
        return ans

m = 4
n = 6
guards = [[0,0],[1,1],[2,3]]
walls = [[0,1],[2,2],[1,4]]

obj = Solution()
result = obj.countUnguarded(m, n, guards, walls)
print(result)
