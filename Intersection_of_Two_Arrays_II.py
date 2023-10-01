class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        
        if (len(nums1) < len(nums2)):
            smallList = nums1
            bigList = nums2
        else:
            smallList = nums2
            bigList = nums1

        ansList = []

        for element in smallList:

            if (element in bigList):
                ansList.append(element)
                bigList.pop(bigList.index(element))

        return ansList

nums1 = [1,2,2,1]
nums2 = [2,2]
obj = Solution()
solution = obj.intersect(nums1, nums2)
print(solution)
