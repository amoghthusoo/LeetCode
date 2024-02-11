class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        
        interDict = dict()

        for item in items1:
            
            if (item[0] not in interDict):
                interDict[item[0]] = item[1]
            else:
                interDict[item[0]] += item[1]
        
        for item in items2:
            
            if (item[0] not in interDict):
                interDict[item[0]] = item[1]
            else:
                interDict[item[0]] += item[1]
        
        outList = []

        for key, value in interDict.items():
            outList.append([key, value])
        
        outList.sort()

        return outList
    

items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]
obj = Solution()
solution = obj.mergeSimilarItems(items1, items2)
print(solution)