class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        i = 0
        while(i < 9):
            visited = set()

            j = 0
            while(j < 9):
                
                e = board[i][j]

                if(e == "."):
                    j += 1
                    continue
                

                if(e not in visited):
                    visited.add(e)
                else:
                    return False

                j += 1
            i += 1

        
        j = 0
        while(j < 9):

            visited = set()

            i = 0
            while(i < 9):

                e = board[i][j]

                if(e == "."):
                    i += 1
                    continue

                if(e not in visited):
                    visited.add(e)
                else:
                    return False

                i += 1
            j += 1

        x = 0
        while(x < 9):
            y = 0
            while(y < 9):

                visited = set()
                i = 0
                while(i < 3):
                    j = 0
                    while(j < 3):

                        target_x = x + i
                        target_y = y + j
                        e = board[target_x][target_y]

                        if(e == "."):
                            j += 1
                            continue

                        if(e not in visited):
                            visited.add(e)
                        else:
                            return False

                        j += 1
                    i += 1

                y += 3
            x += 3
        
        return True