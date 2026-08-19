class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        intr = nums1_set.intersection(nums2_set)

        if(len(intr) != 0):
            return sorted(list(intr))[0]

        else:
            nums1.sort()
            nums2.sort()

            x = nums1[0]
            y = nums2[0]

            if(x <= y):
                return x * 10 + y
            else:
                return y * 10 + x

        