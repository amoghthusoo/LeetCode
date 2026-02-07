class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        
        result = [None for _ in range(len(nums))]

        for i, e in enumerate(nums):

            if(e > 0):
                result[i] = nums[(i + e) % len(nums)] 
            elif(e < 0):
                result[i] = nums[(i - abs(e)) % len(nums)] 
            else:
                result[i] = nums[i]

        return result          