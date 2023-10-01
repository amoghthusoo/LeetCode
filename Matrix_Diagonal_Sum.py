import numpy as np
class Solution:
    def diagonalSum(self, mat: list) -> int:
        
        npMat1 = np.array(mat)
        
        for i in range(len(mat)):
            mat[i].reverse()

        npMat2 = np.array(mat)


        diagonalSum = np.trace(npMat1) + np.trace(npMat2)
        
        if (len(mat) % 2 != 0):
            diagonalSum -= mat[len(mat)//2][len(mat)//2]

        return diagonalSum

mat = [[5]]
obj = Solution()
solution = obj.diagonalSum(mat)
print(solution)