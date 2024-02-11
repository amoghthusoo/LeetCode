class Solution:
    def findRestaurant(self, list1: list, list2: list) -> list:
        
        solDict : dict = {}
        solList : list = []

        i = 0
        while (i < len(list1)):
            
            j = 0
            while (j < len(list2)):
                if (list1[i] == list2[j]):
                    solDict[list1[i]] = i + j
                j += 1
            
            i += 1

        minSumOfIndex = min(solDict.values())

        for key in solDict:

            if (solDict[key] == minSumOfIndex):
                solList.append(key)

        return solList





list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]
obj = Solution()
solution = obj.findRestaurant(list1, list2)
print(solution)