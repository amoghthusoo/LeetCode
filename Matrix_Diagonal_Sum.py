class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        
        _sum = 0
        i = 0
        while(i < len(mat)):
            _sum += mat[i][i] + mat[len(mat) - 1 - i][i]
            i += 1
        
        if(len(mat) % 2 != 0):
            _sum -= mat[len(mat)//2][len(mat)//2]
        
        return _sum