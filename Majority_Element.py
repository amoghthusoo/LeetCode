from collections import Counter
class Solution:
    
    def majorityElement(self, nums: list) -> int:
        
        occDict : dict = Counter(nums)
        numList : list = []
        occList : list = []
        for key in occDict:
            numList.append(key)
            occList.append(occDict[key])

        return numList[occList.index(max(occList))]


nums = [2,2,1,1,1,2,2]
obj = Solution()
solution = obj.majorityElement(nums)
print(solution)