from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: list) -> int:
        
        occDict = dict(Counter(nums))

        for key in occDict:
            
            if occDict[key] == len(nums)/2:
                return key


nums = [5,1,5,2,5,3,5,4]
obj = Solution()
solution = obj.repeatedNTimes(nums)
print(solution)