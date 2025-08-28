from sortedcontainers import SortedList

class Solution:
    def sortMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        
        diagonal_dict = dict()

        for i, row in enumerate(grid):
            for j, e in enumerate(row):

                if(i - j not in diagonal_dict):
                    diagonal_dict[i - j] = SortedList([e])
                else:
                    diagonal_dict[i - j].add(e)

        for i, row in enumerate(grid):
            for j, e in enumerate(row):

                if(i < j):
                    grid[i][j] = diagonal_dict[i - j].pop(0)
                else:
                    grid[i][j] = diagonal_dict[i - j].pop()
        
        return grid

grid = [[1,7,3],[9,8,2],[4,5,6]]
obj = Solution()
result = obj.sortMatrix(grid)
print(result)
