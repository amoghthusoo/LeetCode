import numpy as np
class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        
        interList = []

        for word in strs:
            interList.append(list(word))
        
        interList = np.array(interList)
        interList = interList.transpose()

        count = 0

        for row in interList:

            i = 0
            while(i <= len(row) - 2):

                if(row[i] > row[i + 1]):
                    count += 1
                    break

                i += 1

        return count        

strs = ["zyx","wvu","tsr"]
obj = Solution()
solution = obj.minDeletionSize(strs)
print(solution)