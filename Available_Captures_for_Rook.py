class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        
        for i in range(8):
            for j in range(8):
                if(board[i][j] == "R"):
                    rook_index = [i, j]
        
        ans = 0

        i = rook_index[0]
        j = rook_index[1]

        # Right
        while(j < 8):

            if(board[i][j] == "p"):
                ans += 1
                break
            elif(board[i][j] == "B"):
                break
            
            j += 1

        i = rook_index[0]
        j = rook_index[1]
        # Left
        while(j >= 0):
            
            if(board[i][j] == "p"):
                ans += 1
                break
            elif(board[i][j] == "B"):
                break
            
            j -= 1

        i = rook_index[0]
        j = rook_index[1]
        # Down
        while(i < 8):

            if(board[i][j] == "p"):
                ans += 1
                break
            elif(board[i][j] == "B"):
                break
            
            i += 1

        i = rook_index[0]
        j = rook_index[1]
        # Up
        while(i >= 0):

            if(board[i][j] == "p"):
                ans += 1
                break
            elif(board[i][j] == "B"):
                break
            
            i -= 1

        return ans