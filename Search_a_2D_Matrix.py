class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        
        for row in matrix:
            if target in row:
                return True
        
        return False

nums = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
obj = Solution()
solution = obj.searchMatrix(nums, target)
print(solution)