class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        
        ansNum = 0
        while (len(grid[0]) != 0):

            interList = []

            for element in grid:
                interList.append(element.pop(element.index(max(element))))
            
            ansNum += max(interList)
            interList = []

        return ansNum



grid = [[10]]
obj = Solution()
solution = obj.deleteGreatestValue(grid)
print(solution)