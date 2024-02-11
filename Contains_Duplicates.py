from collections import Counter
class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        
        occDict : dict = dict(Counter(nums))

        occList : list = list(occDict.values())
        occList.sort()

        if (occList[-1] >= 2):
            return True
        else:
            return False

nums = [1,1,1,3,3,4,3,2,4,2]
obj = Solution()
solution = obj.containsDuplicate(nums)
print(solution)