import numpy as np

class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        
        i = 0
        while(i < len(matrix)):

            x = 1
            while(x <= len(matrix)):

                if(x not in matrix[i]):
                    return False
                
                x += 1

            i += 1

        trans_matrix = np.array(matrix).transpose()

        i = 0
        while(i < len(trans_matrix)):

            x = 1
            while(x <= len(trans_matrix)):

                if(x not in trans_matrix[i]):
                    return False
                
                x += 1
            i += 1

        return True

        