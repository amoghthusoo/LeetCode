class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        
        out_arr = [[None for _ in range(len(colSum))] for _ in range(len(rowSum))]

        i = 0
        while(i < len(rowSum)):

            j = 0
            while(j < len(colSum)):

                min_element = min(rowSum[i], colSum[j])
                out_arr[i][j] = min_element
                
                rowSum[i] -= min_element
                colSum[j] -= min_element

                j += 1
            i += 1

        return out_arr
    
rowSum = [5,7,10]
colSum = [8,6,8]
obj = Solution()
out = obj.restoreMatrix(rowSum, colSum)
print(out)