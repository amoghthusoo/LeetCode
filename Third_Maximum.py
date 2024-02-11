from collections import Counter
class Solution:
    def thirdMax(self, nums: list) -> int:
        
        occDict : dict = dict(Counter(nums))
        numList : list = list(occDict.keys())
        numList.sort()
        
        if (len(numList) < 3):
            return numList[-1]
        else:
            return numList[-3]




nums = [2,2,3,1]
obj = Solution()
solution = obj.thirdMax(nums)
print(solution)