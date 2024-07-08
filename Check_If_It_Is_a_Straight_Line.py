class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        
        if(len(coordinates) == 2):
            return True
        
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]

        x2 = coordinates[1][0]
        y2 = coordinates[1][1]

        try:
            m = (y2 - y1) / (x2 - x1)
            c = y1 - m * x1
        except:
            m = c = None



        if(m == None):

            ref_x = coordinates[0][0]
            i = 2
            while(i < len(coordinates)):

                if(coordinates[i][0] != ref_x):
                    return False

                i += 1
            
        
        else:      

            i = 2
            while(i < len(coordinates)):

                if(coordinates[i][1] != m * coordinates[i][0] + c):
                    return False

                i += 1

        return True