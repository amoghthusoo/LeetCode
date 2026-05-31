class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        
        nums = set(nums)

        i = 1
        while(True):

            mul = k * i

            if(mul not in nums):
                return mul
            
            i += 1
            