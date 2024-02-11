from collections import Counter
class Solution:
    def kthDistinct(self, arr: list, k: int) -> str:
        
        occDict = Counter(arr)
        interList = []

        for key in occDict:
            if occDict[key] == 1:
                interList.append(key)

        if (k > len(interList)):
            return ""
        else:
            return interList[k - 1]

arr = ["a","b","a"]
k = 3
obj = Solution()
solution = obj.kthDistinct(arr, k)
print(solution)