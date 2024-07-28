class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        

        occr_dict = {}

        i = 0
        while(i < len(grid)):

            j = 0
            while(j < len(grid)):

                if(grid[i][j] not in occr_dict):
                    occr_dict[grid[i][j]] = 1
                else:
                    occr_dict[grid[i][j]] += 1

                j += 1
            i += 1

        out_arr = [None, None]

        i = 1
        while(i <= int(len(grid) ** 2)):
            
            if(i not in occr_dict):
                out_arr[1] = i

            elif(occr_dict[i] == 2):
                out_arr[0] = i

            
            
            
            i += 1

        return out_arr

