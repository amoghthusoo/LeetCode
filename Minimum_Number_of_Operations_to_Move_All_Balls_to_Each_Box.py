from math import fabs
class Solution:
    def minOperations(self, boxes: str) -> list:
        
        ansList = []

        i = 0
        while (i < len(boxes)):
            
            j = 0
            noOfSteps = 0
            while (j < len(boxes)):
                
                if (j != i and boxes[j] != '0'):
                    noOfSteps += int(fabs(i - j))

                j += 1

            ansList.append(noOfSteps)          
            i += 1

        return ansList

boxes = "001011"
obj = Solution()
solution = obj.minOperations(boxes)
print(solution)