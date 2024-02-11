from itertools import permutations
from collections import Counter
class Solution:
    def permuteUnique(self, nums: list) -> list:
        
        allComb = list(permutations(nums))
        occDict = dict(Counter(allComb)) 
        allComb = list(occDict.keys())

        permuteList = []
        for i in allComb:
            permuteList.append(list(i))
    
        return permuteList

nums = [1,1,2]
obj = Solution()
solution = obj.permuteUnique(nums)
print(solution)