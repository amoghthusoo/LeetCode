# NOT SOLVED
from collections import Counter
class Solution:
    def frequencySort(self, nums: list) -> list:
        
        ansList = []
        occDict = dict(Counter(nums))
        
        freqDict = dict(zip(list(occDict.values()), list(occDict.keys())))

        freqSortList = list(freqDict.keys())
        freqSortList.sort()

        for frequency in freqSortList:

            for i in range(frequency):
                ansList.append(freqDict[frequency])

       
        return ansList


nums = [2,3,1,3,2]
obj = Solution()
solution = obj.frequencySort(nums)
print(solution)