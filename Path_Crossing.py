class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        co_dict = {(0, 0) : None}

        pos = [0, 0]
        for d in path:

            if(d == "E"):
                temp = (pos[0] + 1, pos[1])
                pos[0] += 1
                
            elif(d == "W"):
                temp = (pos[0] - 1, pos[1])
                pos[0] -= 1

            elif(d == "N"):
                temp = (pos[0], pos[1] + 1)
                pos[1] += 1
            
            else:
                temp = (pos[0], pos[1] - 1)
                pos[1] -= 1

            if(temp in co_dict):
                    return True
            else:
                co_dict[temp] = None

        return False
