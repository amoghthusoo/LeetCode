from collections import Counter
class Solution:
    def findDuplicates(self, nums: list) -> list:
        
        ansList = []
        occDict = dict(Counter(nums))

        for key in occDict:

            if occDict[key] == 2:
                ansList.append(key)

        return ansList
    
nums = [1]
obj = Solution()
solution = obj.findDuplicates(nums)
print(solution)