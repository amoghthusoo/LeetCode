class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for element in nums2:
            nums1[nums1.index(0)] = element

        nums1.sort()
        
        return nums1

nums1 = [0]
m = 0
nums2 = [1]
n = 1
obj = Solution()
solution = obj.merge(nums1, m, nums2, n)
print(solution)