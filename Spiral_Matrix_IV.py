# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SpiralMatrix:

    def __init__(self, m, n):
        self.matrix = [[-1 for _ in range(n)] for _ in range(m)]
        self.top_bound = 1
        self.bottom_bound = m - 1
        self.right_bound = n - 1
        self.left_bound = 0
        self.vector = "right"
        self.i = -1
        self.j = -1
        self.init_mem = True

    def insert(self, val):

        if(self.vector == "right"):
            
            if(self.init_mem):
                self.i += 1
                self.j += 1
                self.init_mem = False
            else:
                self.j += 1

            if(self.j <= self.right_bound):
                self.matrix[self.i][self.j] = val
            else:
                self.j -= 1
                self.right_bound -= 1
                self.vector = "down"
                self.insert(val)
            
        elif(self.vector == "down"):
            
            self.i += 1

            if(self.i <= self.bottom_bound):
                self.matrix[self.i][self.j] = val
            else:
                self.i -= 1
                self.bottom_bound -= 1
                self.vector = "left"
                self.insert(val)

        elif(self.vector == "left"):
            
            self.j -= 1

            if(self.j >= self.left_bound):
                self.matrix[self.i][self.j] = val
            else:
                self.j += 1
                self.left_bound += 1
                self.vector = "up"
                self.insert(val)

        elif(self.vector == "up"):
            
            self.i -= 1

            if(self.i >= self.top_bound):
                self.matrix[self.i][self.j] = val
            else:
                self.i += 1
                self.top_bound += 1
                self.vector = "right"
                self.insert(val)
    
    def show(self):

        i = 0
        while(i < len(self.matrix)):
            
            j = 0
            while(j < len(self.matrix[0])):
                
                print(self.matrix[i][j], end=" ")
                j += 1

            print()
            i += 1

class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> list[list[int]]:
        
        out_matrix = SpiralMatrix(m, n)

        traversePtr = head

        while(traversePtr != None):
            out_matrix.insert(traversePtr.val)
            traversePtr = traversePtr.next

        return out_matrix.matrix

m = 3
n = 5
matrix = SpiralMatrix(m, n)
matrix.show()