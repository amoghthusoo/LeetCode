from math import fabs
class Solution:
    def leftRightDifference(self, nums: list) -> list:
        
        ansList = []
        
        i = 0
        while (i < len(nums)):
            leftList = nums[0:i]
            rightList = nums[i + 1 : ]
            ansList.append(int(fabs(sum(leftList) - sum(rightList))))

            i += 1
        
        return ansList



nums = [8,28,35,21,13,21,72,35,52,74]
obj = Solution()
solution = obj.leftRightDifference(nums)
print(solution)

