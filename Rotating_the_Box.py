import numpy as np

class Solution:

    def get_rotated_list(self, line : list[str]) -> list[str]:
        intr_dict = {}

        empty = 0
        stones = 0

        i = 0
        while(i < len(line)):

            entity = line[i]
            if(entity == "."):
                empty += 1
            elif(entity == "#"):
                stones += 1
            else:
                intr_dict[i] = [empty, stones]
                empty = 0
                stones = 0

            i += 1

        intr_dict[i] = [empty, stones]
        
        # print(intr_dict)

        rotated = []
        for key, val in intr_dict.items():
            obstacle = key
            spaces = val[0]
            stones = val[1]

            for _ in range(spaces):
                rotated.append(".")
            
            for _ in range(stones):
                rotated.append("#")
            
            if(len(rotated) < len(line)):
                rotated.append("*")

        return rotated

    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        
        pre_output = []
        for row in boxGrid:
            pre_output.insert(0, self.get_rotated_list(row))

        pre_output = np.array(pre_output).transpose().tolist()
    
        return pre_output

        

boxGrid = [["#",".","*","."],
              ["#","#","*","."]]
solution = Solution()
result = solution.rotateTheBox(boxGrid)
print(result)
