class Solution:
    def maxArea(self, height: list) -> int:
        
        # allPossibleAreas : list = []
        # i = 0
        # while (i < len(height)):
        #     j = i + 1
        #     while (j < len(height)):
                
        #         area = min(height[i], height[j]) * (j - i)
        #         if (len(allPossibleAreas) == 0):
        #             allPossibleAreas.append(area)
        #         elif (area > max(allPossibleAreas)):
        #             allPossibleAreas.append(area)
            
        #         j += 1
        #     i += 1

        # return max(allPossibleAreas)

        intermediateList = []

        i = 0
        j = len(height) - 1

        decisionList = [0, 0]
        while (i <= j):

            intermediateList.append(min(height[i], height[j]) * (j - i))
            
            if (height[i] < height[j]):
                i += 1
            else:
                j -= 1

        intermediateList.sort()
        return intermediateList[-1]

height = [2,3,4,5,18,17,6]
obj = Solution()
solution = obj.maxArea(height)
print(solution)

