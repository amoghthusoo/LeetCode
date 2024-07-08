class Solution:

    def rotate90(self, mat):
        
        out_mat = [[None for _ in range(len(mat))] for _ in range(len(mat))]

        x = 0
        j = 0
        while(j < len(mat)):
            
            y = 0
            i = len(mat) - 1
            while(i >= 0):

                out_mat[x][y] = mat[i][j]

                i -= 1
                y += 1
            
            j += 1
            x += 1

        return out_mat

    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:

        if(mat == target):
            return True
        
        for i in range(3):
            mat = self.rotate90(mat)

            if(mat == target):
                return True
            
        return False

mat = [[0,1],[1,0]]
target = [[1,0],[0,1]]
obj = Solution()
out = obj.findRotation(mat, target)
print(out)