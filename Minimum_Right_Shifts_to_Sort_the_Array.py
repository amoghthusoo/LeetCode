from collections import deque
class Solution:
    
    def is_sorted(self, arr):

        i = 1
        while(i < len(arr)):

            if(arr[i] < arr[i - 1]):
                return False

            i += 1  
        
        return True
    
    def minimumRightShifts(self, nums: list[int]) -> int:
        
        nums = deque(nums)

        i = 0
        while(i <= len(nums) - 1):

            if(self.is_sorted(nums)):
                return i 

            nums.appendleft(nums.pop())             

            i += 1
        
        return -1


nums = [3,4,5,1,2]
obj = Solution()
result = obj.minimumRightShifts(nums)
xprint(result)