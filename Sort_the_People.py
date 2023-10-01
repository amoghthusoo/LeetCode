class Solution:
    def sortPeople(self, names: list, heights: list) -> list:
        
        heightDict = dict(zip(heights, names))

        heights.sort()
        heights.reverse()

        ansList = [heightDict[height] for height in heights]

        return ansList 



names = ["Alice","Bob","Bob"]
heights = [155,185,150]
obj = Solution()
solution = obj.sortPeople(names, heights)
print(solution)