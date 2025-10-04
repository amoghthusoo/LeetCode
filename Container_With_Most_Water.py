class Solution:
    def maxArea(self, height: list) -> int:

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

