class SpiralMatrix:

    def __init__(self, matrix, m, n):
        self.matrix = matrix
        self.top_bound = 1
        self.bottom_bound = m - 1
        self.right_bound = n - 1
        self.left_bound = 0
        self.vector = "right"
        self.i = -1
        self.j = -1
        self.init_mem = True
        self.out = []

    def traverse(self):

        if(self.vector == "right"):
            
            if(self.init_mem):
                self.i += 1
                self.j += 1
                self.init_mem = False
            else:
                self.j += 1

            if(self.j <= self.right_bound):
                self.out.append(self.matrix[self.i][self.j])
            else:
                self.j -= 1
                self.right_bound -= 1
                self.vector = "down"
                self.traverse()
            
        elif(self.vector == "down"):
            
            self.i += 1

            if(self.i <= self.bottom_bound):
                self.out.append(self.matrix[self.i][self.j])
            else:
                self.i -= 1
                self.bottom_bound -= 1
                self.vector = "left"
                self.traverse()

        elif(self.vector == "left"):
            
            self.j -= 1

            if(self.j >= self.left_bound):
                self.out.append(self.matrix[self.i][self.j])
            else:
                self.j += 1
                self.left_bound += 1
                self.vector = "up"
                self.traverse()

        elif(self.vector == "up"):
            
            self.i -= 1

            if(self.i >= self.top_bound):
                self.out.append(self.matrix[self.i][self.j])
            else:
                self.i += 1
                self.top_bound += 1
                self.vector = "right"
                self.traverse()
    
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

        m = len(matrix)
        n = len(matrix[0])

        obj = SpiralMatrix(matrix, m, n)
        
        for _ in range(m * n):
            obj.traverse()
        
        return obj.out

matrix = [[1,2,3],[4,5,6],[7,8,9]]
obj = Solution()
out = obj.spiralOrder(matrix)
print(out)
