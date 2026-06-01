class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        
        i = len(nums) - 1
        while(i >= 0):
            nums.append(nums[i])
            i -= 1
        
        return nums