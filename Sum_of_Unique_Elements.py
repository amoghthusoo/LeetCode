from collections import Counter
class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        
        occDict = dict(Counter(nums))

        interList = []

        for key in occDict:
            
            if (occDict[key] == 1):
                interList.append(key)
        
        return sum(interList)

nums = [1,2,3,4,5]
obj = Solution()
solution = obj.sumOfUnique(nums)
print(solution)