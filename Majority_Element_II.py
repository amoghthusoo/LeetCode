from collections import Counter
from math import floor

class Solution:
    
    def majorityElement(self, nums: list) -> list:
        
        occDict : dict = dict(Counter(nums))
        ansList = []
        for key in occDict:

            if (occDict[key] > floor(len(nums)/3)):
                ansList.append(key)

        return ansList

nums = [1,2]
obj = Solution()
solution = obj.majorityElement(nums)
print(solution)