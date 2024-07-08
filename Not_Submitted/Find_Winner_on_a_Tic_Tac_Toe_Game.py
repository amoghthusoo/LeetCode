class Solution:

    def checkWinner(self, grid, player):

        if(grid[0] == [player, player, player] or
           grid[1] == [player, player, player] or
           grid[2] == [player, player, player] or
           
           grid[0][0] == grid[1][0] == grid[2][0] == player or
           grid[0][1] == grid[1][1] == grid[2][1] == player or
           grid[0][2] == grid[1][2] == grid[2][2] == player or
           
           grid[0][0] == grid[1][1] == grid[2][2] == player or
           grid[0][2] == grid[1][1] == grid[2][0] == player
           ):
            
            return True
        else:
            return False

    def checkPending(self, grid):

        if(None in grid[0] or None in grid[1] or None in grid [2]):
            return True
        else:
            return False
        
    def tictactoe(self, moves: list[list[int]]) -> str:
        
        grid = [[None for _ in range(3)] for _ in range(3)]

        turn = True
        for move in moves:

            if(turn):
                grid[move[0]][move[1]] = True
                turn = False
            else:
                grid[move[0]][move[1]] = False
                turn = True

        if(self.checkWinner(grid, True)):
            return "A"
        elif(self.checkWinner(grid, False)):
            return "B"
        else:
            if(self.checkPending(grid)):
                return "Pending"
            else:
                return "Draw"

        

moves = [[0,0],[1,1]]
obj = Solution()
out = obj.tictactoe(moves)
print(out)           