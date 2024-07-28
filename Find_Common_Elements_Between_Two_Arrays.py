class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        nums1_dict = {}
        nums2_dict = {}

        for num in nums1:
            nums1_dict[num] = None

        for num in nums2:
            nums2_dict[num] = None

        ans1 = 0

        for num in nums1:

            if(num in nums2_dict):
                ans1 += 1

        ans2 = 0

        for num in nums2:

            if(num in nums1_dict):
                ans2 += 1

        return [ans1, ans2]