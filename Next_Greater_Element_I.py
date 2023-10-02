class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        def hasNextGreater(arr, num):

            for element in arr:

                if(element > num):
                    return element
            
            return -1
        
        outList = list()

        for element in nums1:
            outList.append(hasNextGreater(nums2[nums2.index(element) + 1 : ], element))
            
        return outList

nums1 = [4,1,2]
nums2 = [1,3,4,2]
obj = Solution()
solution = obj.nextGreaterElement(nums1, nums2)
print(solution)