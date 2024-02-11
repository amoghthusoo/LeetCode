from collections import Counter
class Solution:
    def findDifference(self, nums1: list, nums2: list) -> list:
        
        ansList = [[], []]

        for element in nums1:
            if element not in nums2:
                ansList[0].append(element)

        for element in nums2:
            if element not in nums1:
                ansList[1].append(element)
        
        ansList = [list(dict(Counter(ansList[0])).keys()), list(dict(Counter(ansList[1])).keys())]

        return ansList

nums1 = [1,2,3]
nums2 = [2,4,6]
obj = Solution()
solution = obj.findDifference(nums1, nums2)
print(solution)