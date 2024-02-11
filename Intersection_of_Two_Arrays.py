from collections import Counter
class Solution:
    def intersection(self, nums1: list, nums2: list) -> list:
        
        intersectionWithDuplicates : list = []

        for element in nums1:
            
            if (element in nums2):
                intersectionWithDuplicates.append(element)

        occDict : dict = dict(Counter(intersectionWithDuplicates))

        return list(occDict.keys())

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
obj = Solution()
solution = obj.intersection(nums1, nums2)
print(solution)