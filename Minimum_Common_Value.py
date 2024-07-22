class Solution:

    def ifExists(self, arr, target) -> bool:

        i = 0
        while(i < len(arr)):
            

            if(arr[i] == target):
                return True

            if(arr[i] > target):
                return False
            
            i += 1

        return False
        

    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        
        i = 0
        while(i < len(nums1)):
            
            if(self.ifExists(nums2, nums1[i])):
                return nums1[i]
            
            i += 1
        
        return -1