from collections import deque

class Solution:

    def __init__(self):
        self.U = set([str(i) for i in range(1, 10)])

    def get_possibility_vector(self, board, i, j):
        
        not_possible = set()

        x = 0
        while(x < 9):
            e = board[i][x]
            if(e != "."):
                not_possible.add(e)
            x += 1
        
        x = 0
        while(x < 9):
            e = board[x][j]
            if(e != "."):
                not_possible.add(e)
            x += 1
        
        _i = i - (i % 3)
        _j = j - (j % 3)

        x = 0
        while(x < 3):
            y = 0
            while(y < 3):
                
                e = board[_i + x][_j + y]

                if(e != "."):
                    not_possible.add(e)

                y += 1
            x += 1

        return deque(self.U.difference(not_possible))

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        stack = deque()

        i = 0
        while(i < 9):
            
            j = 0
            while(j < 9):
                if(board[i][j] == "."):
                    pv = self.get_possibility_vector(board, i, j)

                    if(len(pv) == 0):
                        
                        while(True):
                            popped = stack.pop()
                            i = popped[0]
                            j = popped[1]
                            pv = popped[2]

                            if(len(pv) == 0):
                                board[i][j] = "."
                            else:
                                break
                        
                        e = pv.popleft()
                        board[i][j] = e
                        stack.append((i, j, pv))

                    else:
                        
                        e = pv.popleft()
                        board[i][j] = e
                        stack.append((i, j, pv))

                j += 1
            i += 1


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
obj = Solution()
obj.solveSudoku(board)
for row in board:
    print(row)