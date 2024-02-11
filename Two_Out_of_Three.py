class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        
        outList = list()

        for element in nums1:

            if (element in nums2 or element in nums3):
                outList.append(element)

        for element in nums2:

            if (element in nums1 or element in nums3):
                outList.append(element)

        return list(set(outList))


nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
obj = Solution()
solution = obj.twoOutOfThree(nums1, nums2, nums3)
print(solution)
