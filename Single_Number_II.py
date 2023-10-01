from collections import Counter
class Solution:
    def singleNumber(self, nums: list) -> int:
        
        occDict = dict(Counter(nums))

        for key in occDict:
            if(occDict[key] == 1):
                return key

nums = [0,1,0,1,0,1,99]
obj = Solution()
solution = obj.singleNumber(nums)
print(solution)