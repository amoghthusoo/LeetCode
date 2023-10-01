from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: list) -> int:

        occDict = Counter(arr)

        for key in occDict:
            
            if (occDict[key]/len(arr) * 100 > 25):
                return key

arr = [1,2,2,6,6,6,6,7,10]
obj = Solution()
solution = obj.findSpecialInteger(arr)
print(solution)