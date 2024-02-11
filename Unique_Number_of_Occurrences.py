from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        
        occDict = dict(Counter(arr))
        occOccDict = dict(Counter(list(occDict.values())))
        occOccValuesList = list(occOccDict.values())

        if (occOccValuesList.count(1) != len(occOccDict)):
            return False
        else:
            return True      



arr = [-3,0,1,-3,1,1,1,-3,10,0]
obj = Solution()
solution = obj.uniqueOccurrences(arr)
print(solution)