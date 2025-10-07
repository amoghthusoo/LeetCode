class Solution:

    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        
        occr_dict = dict()

        i = 0
        while(i < len(matrix)):

            previous = matrix[i][0]
            count = 0
            temp_list = []

            j = 0
            while(j < len(matrix[0])):

                if(matrix[i][j] == previous):
                    count += 1

                else:
                    temp_list.append(count)
                    previous = matrix[i][j]
                    count = 1   

                j += 1

            temp_list.append(count)
            temp_tuple = tuple(temp_list)

            if(temp_tuple not in occr_dict):
                occr_dict[temp_tuple] = 1
            else:
                occr_dict[temp_tuple] += 1 
            
            i += 1

        return max(occr_dict.values())

matrix = [[0,1],[1,1]]
solution = Solution()
result = solution.maxEqualRowsAfterFlips(matrix)
print(result)