from statistics import median
class Solution:
    
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        
        return median(sorted(nums1 + nums2))
        

nums1 = [1,2]
nums2 = [3,4]
obj = Solution()
solution = obj.findMedianSortedArrays(nums1, nums2)
print(solution)