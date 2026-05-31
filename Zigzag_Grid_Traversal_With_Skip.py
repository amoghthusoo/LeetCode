class Solution:
    def zigzagTraversal(self, grid: list[list[int]]) -> list[int]:
        
        ans = []
        i = 0
        while(i < len(grid)):

            if(i % 2 == 0):
                j = 0
            else:
                j = 1

            temp = []
            while(j < len(grid[0])):

                temp.append(grid[i][j])
                j += 2
            
            if(i % 2 == 0):
                ans.extend(temp)
            else:
                temp.reverse()
                ans.extend(temp)

            i += 1
        
        return ans

grid = [[1,2,3],[4,5,6],[7,8,9]]
obj = Solution()
result = obj.zigzagTraversal(grid)
print(result)