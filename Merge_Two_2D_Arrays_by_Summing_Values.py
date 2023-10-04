class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        
        interDict = {}

        for subarr in nums1:

            if(subarr[0] not in interDict):
                interDict[subarr[0]] = subarr[1]
            else:
                interDict[subarr[0]] += subarr[1]
        
        for subarr in nums2:

            if(subarr[0] not in interDict):
                interDict[subarr[0]] = subarr[1]
            else:
                interDict[subarr[0]] += subarr[1]

        interList = [[key, value] for key, value in interDict.items()]
        
        return sorted(interList)

nums1 = [[2,4],[3,6],[5,5]]
nums2 = [[1,3],[4,3]]
obj = Solution()
solution = obj.mergeArrays(nums1, nums2)
print(solution)