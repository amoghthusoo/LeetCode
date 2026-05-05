class Solution:
    def findColumnWidth(self, grid: list[list[int]]) -> list[int]:
        
        ans = []

        for j in range(len(grid[0])):
            max_len = 0
            for i in range(len(grid)):
                temp_len = len(str(grid[i][j]))
                if(temp_len > max_len):
                    max_len = temp_len
            ans.append(max_len)

        return ans
                    