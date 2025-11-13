class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        
        for i in range(len(nums) - 1):
            if(nums[i] == nums[i + 1]):
                nums[i] *= 2
                nums[i + 1] = 0
        
        ans = []
        for e in nums:
            if(e != 0):
                ans.append(e)
        
        zero_count = len(nums) - len(ans)
        ans.extend([0 for _ in range(zero_count)])

        return ans