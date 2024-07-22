class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:

        count = 0

        i = 0
        while(i < len(nums1)):

            j = 0
            while(j < len(nums2)):

                if(nums1[i] % (nums2[j] * k) == 0):
                    count += 1

                j += 1
            i += 1

        return count