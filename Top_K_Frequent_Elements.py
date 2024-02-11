from collections import Counter
class Solution:
    
    def topKFrequent(self, nums: list, k: int) -> list:
        
        def frequentElement(occDict) -> int:

            maxFreq = max(occDict.values())

            for key in occDict:
                if (occDict[key] == maxFreq):
                    del(occDict[key])
                    return key, occDict 

        occDict = dict(Counter(nums))
        ansList = []

        for i in range(k):
            key, occDict = frequentElement(occDict)
            ansList.append(key)

        return ansList

        


nums = [4, 4, 4, 3, 4, 3, 2, 3, 2, 0]
k = 4
obj = Solution()
solution = obj.topKFrequent(nums, k)
print(solution)