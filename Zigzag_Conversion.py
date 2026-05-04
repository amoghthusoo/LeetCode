class Solution:
    def __init__(self):
        self.i = None
        self.j = None
        self.n = None
        self.m = None
        self.vector = None
        
    def update_pointer(self):
        
        if(self.i == -1):
            self.i = self.j = 0

            if(self.i == self.n - 1):
                self.vector = "diagonal"
            
            return 

        if(self.vector == "down"):
            self.i += 1
            
            if(self.i == self.n - 1):
                self.vector = "diagonal"
            return
        
        if(self.vector == "diagonal"):

            self.i -= 1
            self.j += 1
            
            if(self.i == 0):
                self.vector = "down"
            
            return

    def convert(self, s: str, numRows: int) -> str:

        if(numRows == 1):
            return s        

        self.i = -1
        self.j = -1
        self.n = numRows
        self.m = len(s)
        self.vector = "down"

        mat = [[None for _ in range(len(s))] for _ in range(numRows)]

        for e in s:
            self.update_pointer()
            mat[self.i][self.j] = e

        ans = ""
        for i in range(len(mat)):
            for j in range(len(mat[0])):

                if(mat[i][j] != None):
                    ans += mat[i][j]

        return ans
    
s = "PAYPALISHIRING"
numRows = 3
obj = Solution()
result = obj.convert(s, numRows)
print(result)