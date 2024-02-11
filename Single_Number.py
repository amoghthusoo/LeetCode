from collections import Counter
class Solution:
    def singleNumber(self, nums: list) -> int:
        
        occDict = Counter(nums)

        for key in occDict:

            if occDict[key] == 1:
                return key

nums = [1]
obj = Solution()
solution = obj.singleNumber(nums)
print(solution)