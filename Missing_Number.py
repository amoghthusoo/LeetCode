class Solution:
    def missingNumber(self, nums: list) -> int:
        
        refList = list(range(0, len(nums) + 1))

        for num in refList:

            if num not in nums:
                return num

nums = [9,6,4,2,3,5,7,0,1]
obj = Solution()
solution = obj.missingNumber(nums)
print(solution)