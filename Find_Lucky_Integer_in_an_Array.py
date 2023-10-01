from collections import Counter
class Solution:
    def findLucky(self, arr: list) -> int:
        
        occDict = dict(Counter(arr))
        posAns = []

        for key in occDict:
            if (occDict[key] == key):
                posAns.append(key)
            
        if (len(posAns) != 0):
            return max(posAns)
        else:
            return -1

arr = [2,2,2,3,3]
obj = Solution()
solution = obj.findLucky(arr)
print(solution)